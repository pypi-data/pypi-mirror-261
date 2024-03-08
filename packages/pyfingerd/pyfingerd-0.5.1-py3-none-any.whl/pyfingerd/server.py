#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2023 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Finger server."""

from __future__ import annotations

from abc import ABC as _ABC, abstractmethod as _abstractmethod
import asyncio as _asyncio
from collections.abc import (
    Callable as _Callable,
    Coroutine as _Coroutine,
    Iterable as _Iterable,
)
from datetime import datetime as _datetime
from errno import errorcode as _errorcode
from ipaddress import IPv4Address as _IPv4Address, IPv6Address as _IPv6Address
import multiprocessing as _multip
import signal as _signal
import string as _string
from traceback import format_exc as _format_exc
from typing import ClassVar as _ClassVar, TypeVar as _TypeVar

from croniter import croniter as _croniter
from pydantic import BaseModel as _BaseModel, ConfigDict as _ConfigDict

from .binds import (
    FingerBind as _FingerBind,
    FingerBindsDecoder as _FingerBindsDecoder,
)
from .core import (
    FingerFormatter as _FingerFormatter,
    FingerInterface as _FingerInterface,
)
from .errors import (
    HostnameError as _HostnameError,
    MalformedRequestError as _MalformedRequestError,
    NoBindsError as _NoBindsError,
)
from .utils import (
    access_logger as _access_logger,
    error_logger as _error_logger,
    logger as _logger,
)


__all__ = ["FingerBaseServer", "FingerRequest", "FingerServer"]

_FingerRequestType = _TypeVar("_FingerRequestType", bound="FingerRequest")


class FingerRequest(_BaseModel):
    """A finger query."""

    # "By default, this program SHOULD filter any unprintable data,
    #  leaving only printable 7-bit characters (ASCII 32 through
    #  ASCII 126), tabs (ASCII 9) and CRLFs."
    ALLOWED_CHARS: _ClassVar[str] = (
        "\t !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        + _string.ascii_letters
        + _string.digits
    )

    model_config = _ConfigDict(strict=True, frozen=True)
    """Configuration dictionary for the model."""

    host: str | None = None
    """Host of the query, if the client wants the server to transmit it."""

    query: str | None = None
    """Username query, if provided by the client."""

    verbose: bool = False
    """Whether the client has provided the '/W' or not."""

    line: str
    """The raw query line provided by the client."""

    @classmethod
    def decode(
        cls: type[_FingerRequestType],
        raw: bytes,
        /,
    ) -> _FingerRequestType:
        """Decode a raw finger query.

        There are three types of requests recognized by RFC 1288:

        * {C} is a request for a list of all online users.
        * {Q1} is a request for a local user.
        * {Q2} is a request for a distant user (with hostname).

        /W means the RUIP (program answering the query) should be more
        verbose (this token can be ignored).

        :param line: The line to decode.
        :return: The query.
        """
        # Get a character string out of the query.
        line = "".join(
            char
            for char in raw.decode("ascii", errors="ignore")
            if char in cls.ALLOWED_CHARS
        )

        # Get elements.
        host = None
        username = None
        verbose = False
        for element in line.split():
            if element[0] == "/":
                if not element[1:]:
                    raise _MalformedRequestError(
                        "Missing feature flags after '/'",
                        line=line,
                    )

                for letter in element[1:]:
                    if letter == "W":
                        verbose = True
                    else:
                        raise _MalformedRequestError(
                            f"Unknown feature flag {letter!r}",
                            line=line,
                        )

                continue

            if username is not None:
                raise _MalformedRequestError(
                    "Multiple query arguments",
                    line=line,
                )

            username = element

        if username is not None and "@" in username:
            host, *username_parts = username.split("@")[::-1]
            username = "@".join(username_parts[::-1])

        return cls(
            host=host,
            query=username,
            verbose=verbose,
            line=line,
        )


class FingerBaseServer(_ABC):
    """Base finger server class.

    :param binds: The hosts and ports on which the server should listen to
        and answer finger requests.
    :param debug: Whether the tracebacks should be transmitted back to the
        client or not.
    """

    __slots__ = ("_binds", "_debug", "_p")

    _p: _multip.Process | None
    """Process running the pyfingerd server."""

    def __init__(
        self,
        binds: str = "localhost:79",
        /,
        *,
        debug: bool = False,
    ) -> None:
        decoded_binds = list(_FingerBindsDecoder().decode(binds))
        if not decoded_binds:
            raise _NoBindsError()

        self._p = None
        self._binds = decoded_binds
        self._debug = debug

    @_abstractmethod
    async def handle_malformed_request(
        self,
        /,
        *,
        exc: _MalformedRequestError,
        src: _IPv4Address | _IPv6Address,
    ) -> str:
        """Handle an invalid request.

        :param exc: Raised exception describing the request parsing error.
        :param src: Source from which the request has been emitted.
        :return: ASCII-compatible result.
        """

    @_abstractmethod
    async def handle_request(
        self,
        request: FingerRequest,
        /,
        *,
        src: _IPv4Address | _IPv6Address,
    ) -> str:
        """Handle a valid request.

        :param request: Decoded request.
        :param src: Source from which the request has been emitted.
        :return: ASCII-compatible result.
        """

    async def _handle_async_finger_connection(
        self,
        inp: _asyncio.StreamReader,
        outp: _asyncio.StreamWriter,
        /,
    ) -> None:
        """Handle an asynchronous connection.

        :param inp: The stream reader for the connection.
        :param outp: The stream writer for the connection.
        """
        raw_src, *_ = outp.get_extra_info("peername")

        try:
            src: _IPv4Address | _IPv6Address = _IPv4Address(raw_src)
        except ValueError:
            src = _IPv6Address(raw_src)

        # Gather the request line.
        try:
            line = await inp.readline()
        except ConnectionResetError:
            _error_logger.info(
                "%s submitted no request. (possible scan)",
                src,
            )
            return

        try:
            try:
                request = FingerRequest.decode(line)
            except _MalformedRequestError as exc:
                response_text = await self.handle_malformed_request(
                    exc=exc,
                    src=src,
                )
            else:
                response_text = await self.handle_request(request, src=src)
        except Exception:
            _logger.exception("An error has occurred within the server.")

            if self._debug:
                response_text = "An error has occurred:\n\n" + _format_exc()
            else:
                response_text = "An error has occurred.\n"

        response_text = "\r\n".join(response_text.splitlines()) + "\r\n"
        outp.write(response_text.encode("ascii", errors="ignore"))

    async def _handle_async_connection(
        self,
        inp: _asyncio.StreamReader,
        outp: _asyncio.StreamWriter,
        /,
    ) -> None:
        """Handle a new incoming asynchronous connection.

        :param inp: The stream reader for the connection.
        :param outp: The stream writer for the connection.
        """
        try:
            await self._handle_async_finger_connection(inp, outp)
        except Exception:
            _logger.exception("The following exception has occurred:")

            if not self._debug:
                outp.write(b"An internal exception has occurred.\r\n")
            else:
                traceback = "\r\n  ".join(_format_exc().splitlines())
                outp.write(
                    b"An internal exception has occurred:\r\n\r\n  "
                    + traceback.encode("ascii", errors="ignore")
                    + b"\r\n",
                )

            raise
        finally:
            try:
                outp.close()
                await outp.wait_closed()
            except Exception:
                _logger.exception("Failed closing the connection:")

    async def _start_server_for_bind(self, bind: _FingerBind, /) -> None:
        """Start an asynchronous server."""
        family, host, port = bind.runserver_params

        try:
            server = await _asyncio.start_server(
                self._handle_async_connection,
                host=host,
                port=port,
                family=family,
                reuse_address=True,
            )
        except OSError as exc:
            name = _errorcode[exc.errno]

            if name == "EADDRINUSE":
                _logger.error(
                    "Could not bind to [%s]:%d: address already in use.",
                    host,
                    port,
                )
            elif name == "EACCES":
                _logger.error(
                    "Could not bind to [%s]:%d: port %d is a privileged "
                    + "port and process is unprivileged.",
                    host,
                    port,
                    port,
                )
            elif name == "EADDRNOTAVAIL":
                _logger.error(
                    "Could not bind to [%s]:%d: %s is not "
                    + "available to bind.",
                    host,
                    port,
                    host,
                )
            else:
                raise
        else:
            _logger.info("Starting pyfingerd on [%s]:%d.", host, port)

            try:
                await server.serve_forever()
            except _asyncio.CancelledError:
                pass

            _logger.info("Stopping pyfingerd on [%s]:%d", host, port)

    def prepare_auxiliary_coroutines(self, /) -> _Iterable[_Coroutine]:
        """Get the general coroutines for the server, excluding binds.

        This can be used by the child server to run coroutines aside the
        server coroutines, e.g. workers to update the state.

        By default, this method does not yield any auxiliary coroutine.

        :return: Coroutine iterator.
        """
        return
        yield

    def _prepare_coroutines(self, /) -> _Iterable[_Coroutine]:
        """Prepare coroutines to be run within the server process.

        This prepares one server coroutine per bind, and auxiliary coroutines
        that may be instantiated by :py:meth:`prepare_auxiliary_coroutines`.

        :return: The coroutine iterator.
        """
        for bind in self._binds:
            yield self._start_server_for_bind(bind)

        yield from self.prepare_auxiliary_coroutines()

    async def start_async(self, /) -> None:
        """Start the servers."""
        tasks: tuple[_asyncio.Task, ...] = tuple(
            _asyncio.create_task(co) for co in self._prepare_coroutines()
        )

        await _asyncio.wait(
            tasks,
            return_when=_asyncio.FIRST_COMPLETED,
        )

        # If any task has set an exception, we try to catch it.
        exc = None
        for task in tasks:
            if exc is None:
                try:
                    exc = task.exception()
                except _asyncio.exceptions.InvalidStateError:
                    exc = None

            task.cancel()

        if exc is not None:
            raise exc

    def start_sync(self, /) -> None:
        """Start the coroutines to run the server and background tasks."""
        try:
            _asyncio.run(self.start_async())
        except KeyboardInterrupt:
            pass

    def start(self, /) -> None:
        """Start all underlying server processes and bind all ports."""
        if self._p is not None and self._p.is_alive():
            return

        process = _multip.Process(target=self.start_sync)
        process.start()
        self._p = process

    def stop(self, /) -> None:
        """Stop all underlying server processes and unbind all ports."""
        process = self._p
        if process is None or not process.is_alive():
            return

        process.kill()
        process.join()
        self._p = None

    def serve_forever(self, /) -> None:
        """Start all servers and serve in a synchronous fashion.

        It starts all servers :py:meth:`FingerServer.start`, waits for
        an interrupt signal, and stops all servers using
        :py:meth:`FingerServer.stop`.
        """
        if self._p is not None:
            self.start()

            try:
                while True:
                    _signal.pause()
            except KeyboardInterrupt:
                pass

            self.stop()
        else:
            # If the server hasn't been started on another process
            # using ``.start()``, we can just start is on this process.
            self.start_sync()

    def shutdown(self, /) -> None:
        """Shutdown the server, alias to `.stop()`."""
        self.stop()


class FingerServer(FingerBaseServer):
    """Finger server making use of an interface and a formatter.

    :param binds: The hosts and ports on which the server should listen to
        and answer finger requests.
    :param hostname: The hostname to be included in answers sent to clients.
    :param interface: The interface to use for querying users and sessions.
    :param formatter: The formatter to use for formatting answers sent
        to clients.
    :param debug: Whether the tracebacks should be transmitted back to the
        client or not.
    """

    __slots__ = ("_interface", "_formatter", "_hostname")

    @property
    def hostname(self) -> str:
        """Get the hostname configured for this server."""
        return self._hostname

    @property
    def interface(self) -> _FingerInterface:
        """Get the interface configured for this server."""
        return self._interface

    @property
    def formatter(self) -> _FingerFormatter:
        """Get the formatter configured for this server."""
        return self._formatter

    def __init__(
        self,
        binds: str = "localhost:79",
        /,
        *,
        hostname: str = "LOCALHOST",
        interface: _FingerInterface | None = None,
        formatter: _FingerFormatter | None = None,
        debug: bool = False,
    ):
        super().__init__(binds, debug=debug)

        # Check the host name, which should be simple LDH, i.e.
        # Letters, Digits, Hyphens.
        try:
            hostname = hostname.upper()
            if not all(
                c in _string.ascii_letters + _string.digits + ".-"
                for c in hostname
            ):
                raise AssertionError("Non-LDH hostname")
        except Exception as exc:
            raise _HostnameError(hostname=hostname) from exc

        # Check the interface and formatter classes.
        if interface is None:
            interface = _FingerInterface()
        elif not isinstance(interface, _FingerInterface):
            raise TypeError(
                "Please base your interface "
                + "on the base class provided by the pyfingerd module",
            )

        if formatter is None:
            formatter = _FingerFormatter()
        elif not isinstance(formatter, _FingerFormatter):
            raise TypeError(
                "Please base your formatter "
                + "on the base class provided by the pyfingerd module",
            )

        # Keep the parameters.
        self._hostname = hostname
        self._interface = interface
        self._formatter = formatter

    async def _cron_call(
        self,
        func: _Callable[[], None],
        spec: _croniter,
    ) -> None:
        """Call a function periodically using a cron specification.

        :param func: The function to call periodically.
        :param spec: The croniter specification to follow.
        """
        spec.set_current(_datetime.now())

        while True:
            try:
                func()
            except SystemExit:
                return

            while True:
                seconds = (
                    spec.get_next(_datetime) - _datetime.now()
                ).total_seconds()
                if seconds >= 0:
                    break

            await _asyncio.sleep(seconds)

    def prepare_auxiliary_coroutines(self) -> _Iterable[_Coroutine]:
        """Get the general coroutines for the server, excluding binds.

        We override this method to instanciate a cron per special
        method present in the interface, to allow e.g. updating the
        interface state regularly.

        :return: Coroutine iterator.
        """
        for key in dir(self._interface):
            member = getattr(self._interface, key)
            if not callable(member):
                continue

            try:
                spec = member.__cron__
            except AttributeError:
                continue

            if not isinstance(spec, _croniter):
                continue

            yield self._cron_call(member, spec)

    async def handle_malformed_request(
        self,
        /,
        *,
        exc: _MalformedRequestError,
        src: _IPv4Address | _IPv6Address,
    ) -> str:
        """Handle an invalid request.

        :param exc: Raised exception describing the request parsing error.
        :param src: Source from which the request has been emitted.
        :return: ASCII-compatible result.
        """
        _error_logger.info(
            "%s made a bad request: %s in %r.",
            src,
            exc.msg,
            exc.line,
        )
        return self.formatter.format_query_error(self.hostname, exc.line)

    async def handle_request(
        self,
        request: FingerRequest,
        /,
        *,
        src: _IPv4Address | _IPv6Address,
    ) -> str:
        """Handle a valid request.

        :param request: Decoded request.
        :param src: Source from which the request has been emitted.
        :return: ASCII-compatible result.
        """
        if request.host is not None:
            if request.query:
                _access_logger.info(
                    "%s requested transmitting user query for %r at %r.",
                    src,
                    request.query,
                    request.host,
                )
            else:
                _access_logger.info(
                    "%s requested transmitting user query to %r.",
                    src,
                    request.host,
                )

            return self.interface.transmit_query(
                request.query,
                request.host,
                request.verbose,
            )

        if request.query:
            users = self.interface.search_users(request.query, None)
            _access_logger.info(
                "%s requested user %r: found %s.",
                src,
                request.query,
                {0: "no user", 1: "1 user"}.get(
                    len(users),
                    f"{len(users)} users",
                ),
            )
        else:
            users = self.interface.search_users(None, True)
            _access_logger.info(
                "%s requested connected users: found %s.",
                src,
                {0: "no user", 1: "1 user"}.get(
                    len(users),
                    f"{len(users)} users",
                ),
            )

        if request.query or request.verbose:
            return self.formatter.format_long(
                self.hostname,
                request.line,
                users,
            )

        return self.formatter.format_short(
            self.hostname,
            request.line,
            users,
        )
