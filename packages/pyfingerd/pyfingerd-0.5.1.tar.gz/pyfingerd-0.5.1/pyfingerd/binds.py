#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Binds decoder for the finger server."""

from __future__ import annotations

from collections.abc import Sequence as _Sequence
import socket as _socket

from .errors import InvalidBindError as _InvalidBindError


__all__ = [
    "FingerBind",
    "FingerBindsDecoder",
    "FingerTCPv4Bind",
    "FingerTCPv6Bind",
]


class FingerBind:
    """Bind address for pyfingerd."""

    @property
    def runserver_params(self) -> tuple[_socket.AddressFamily, str, int]:
        """Return the data as ``start_server`` arguments."""
        raise NotImplementedError()


class FingerTCPv4Bind(FingerBind):
    """IPv4 TCP Address."""

    __slots__ = ("_addr", "_port")

    def __init__(self, address: str, port: int):
        self._addr = _socket.inet_pton(_socket.AF_INET, address)
        self._port = port

    @property
    def runserver_params(self) -> tuple[_socket.AddressFamily, str, int]:
        """Return the data as ``start_server`` parameters."""
        return (
            _socket.AF_INET,
            _socket.inet_ntop(_socket.AF_INET, self._addr),
            self._port,
        )


class FingerTCPv6Bind(FingerBind):
    """IPv6 TCP Address."""

    __slots__ = ("_addr", "_port")

    def __init__(self, address: str, port: int):
        self._addr = _socket.inet_pton(_socket.AF_INET6, address)
        self._port = port

    @property
    def runserver_params(self) -> tuple[_socket.AddressFamily, str, int]:
        """Return the data as `start_server` parameters."""
        return (
            _socket.AF_INET6,
            _socket.inet_ntop(_socket.AF_INET6, self._addr),
            self._port,
        )


class FingerBindsDecoder:
    """Binds decoder for pyfingerd."""

    __port__ = ("_proto",)

    def __init__(self, proto: str = "finger"):
        proto = proto.casefold()
        if proto not in ("finger",):
            raise ValueError(f"unsupported protocol {proto!r}")

        self._proto = proto

    def decode(self, raw: str) -> _Sequence[FingerBind]:
        """Get binds for the server, using a given string."""
        binds: set[FingerBind] = set()

        for addr in map(lambda x: x.strip(), raw.split(",")):
            if not addr:
                continue

            # Try to find a scheme.
            scheme, *rest = addr.split(":/")
            if not rest:
                # No scheme found, let's just guess the scheme based on
                # the situation.
                raw = scheme
                scheme = {"finger": "tcp"}[self._proto]
            else:
                # Just don't add the ':' of ':/' again.
                raw = "/" + ":/".join(rest)

            if (self._proto == "finger" and scheme != "tcp") or scheme not in (
                "tcp",
            ):
                raise _InvalidBindError(
                    f"Unsupported scheme {scheme!r} for "
                    + f"protocol {self._proto!r}",
                    bind=addr,
                )

            # Decode the address data.
            if scheme == "tcp":
                binds.update(self._decode_tcp_host(raw))

        return tuple(binds)

    def __repr__(self):
        return f"{self._class__.__name__}()"

    def _decode_tcp_host(self, x: str) -> _Sequence[FingerBind]:
        """Decode suitable hosts for a TCP bind."""
        addr = x

        # TODO: manage the '*' case.
        # TODO: decode hosts without the default host.

        # Get the host part first, we'll decode it later.
        if x[0] == "[":
            # The host part is an IPv6, look for the closing ']' and
            # decode it later.
            to = x.find("]")
            if to < 0:
                raise _InvalidBindError("Expected closing ']'", bind=addr)

            host = x[1:to]
            x = x[to + 1 :]

            is_ipv6 = True
        else:
            # The host part is either an IPv4 or a host name, look for
            # the ':' and decode it later.
            host, *rest = x.split(":")
            x = ":" + ":".join(rest)

            is_ipv6 = False

        # Decode the port part.
        if x in ("", ":"):
            port = 79
        elif x[0] == ":":
            try:
                port = int(x[1:])
            except ValueError:
                try:
                    if x[1:] != "":
                        raise AssertionError("Expected a port number")

                    port = _socket.getservbyname(x[1:])
                except Exception:
                    raise _InvalidBindError(
                        "Expected a valid port number or name "
                        + f"(got {x[1:]!r})",
                        bind=addr,
                    ) from None
        else:
            raise _InvalidBindError("Garbage found after the host", bind=addr)

        # Manage localhost by default.
        if not host:
            host = "localhost"

        # Decode the host part and get the addresses.
        addrs: tuple[FingerBind, ...] = ()
        if is_ipv6:
            # Decode the IPv6 address (validate it using `_socket.inet_pton`).
            ip6 = host
            _socket.inet_pton(_socket.AF_INET6, host)
            addrs += (FingerTCPv6Bind(ip6, port),)
        else:
            # Decode the host (try IPv4, otherwise, resolve domain).
            try:
                ip_parts_s = host.split(".")
                if len(ip_parts_s) < 2 or len(ip_parts_s) > 4:
                    raise _InvalidBindError(
                        f"Expected a valid IP address, got {host!r}.",
                        bind=addr,
                    )

                ip = list(map(int, ip_parts_s))
                if not all(0 <= x < 256 for x in ip):
                    raise _InvalidBindError(
                        f"Expected a valid IP address, got {host!r}.",
                        bind=addr,
                    )

                if len(ip) == 2:
                    ip = [ip[0], 0, 0, ip[1]]
                elif len(ip) == 3:
                    ip = [ip[0], 0, ip[1], ip[2]]

                addrs += (
                    FingerTCPv4Bind(
                        f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}",
                        port,
                    ),
                )
            except Exception:
                try:
                    entries = _socket.getaddrinfo(
                        host,
                        port,
                        proto=_socket.IPPROTO_TCP,
                        type=_socket.SOCK_STREAM,
                    )
                except _socket.gaierror:
                    raise _InvalidBindError(
                        f"Invalid IP address and unresolved host: {host!r}",
                        bind=addr,
                    )

                for ent in entries:
                    if ent[0] not in (
                        _socket.AF_INET,
                        _socket.AF_INET6,
                    ) or ent[1] not in (_socket.SOCK_STREAM,):
                        continue

                    if ent[0] == _socket.AF_INET:
                        addrs += (FingerTCPv4Bind(ent[4][0], port),)
                    else:
                        ip6 = ent[4][0]
                        _socket.inet_pton(_socket.AF_INET6, ent[4][0])
                        addrs += (FingerTCPv6Bind(ip6, port),)

        return addrs
