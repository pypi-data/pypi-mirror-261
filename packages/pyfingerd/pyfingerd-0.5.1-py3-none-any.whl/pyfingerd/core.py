#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2023 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Main classes for the finger server, interfaces and formatters.

These classes, which behave as base returning default data,
are bundled with base definitions for users and sessions.
"""

from __future__ import annotations

from collections.abc import (
    Callable as _Callable,
    Iterator as _Iterator,
    Sequence as _Sequence,
)
from datetime import (
    datetime as _datetime,
    timedelta as _timedelta,
    timezone as _timezone,
    tzinfo as _tzinfo,
)
from typing import Any as _Any

from croniter import croniter as _croniter
from pydantic import (
    AwareDatetime as _AwareDatetime,
    BaseModel as _BaseModel,
    ConfigDict as _ConfigDict,
    field_validator as _field_validator,
    model_validator as _model_validator,
)

from .utils import logger as _logger


__all__ = [
    "FingerFormatter",
    "FingerInterface",
    "FingerSession",
    "FingerUser",
    "cron",
]


def cron(spec: str) -> _Callable[[_Callable], _Callable]:
    """Add a cron specification to the callable.

    This decorator adds the ``__cron__`` member on the callable,
    as a ``croniter`` instance using the given specification.

    This makes the callable identifiable by the finger server when
    starting a server with an interface with such a callable,
    by checking if the attribute exists and starting a dedicated
    coroutine for running it periodically using the given specification.

    :param spec: The cron specification expressed as a string.
    """
    cron_spec = _croniter(spec)

    def decorator(func: _Callable, /) -> _Callable:
        func.__cron__ = cron_spec  # type: ignore
        return func

    return decorator


class FingerSession(_BaseModel):
    """Representation of an active session for a given user on the system."""

    model_config = _ConfigDict(strict=True, frozen=True)
    """Configuration dictionary for the model."""

    start: _AwareDatetime
    """Date and time at which the session has started."""

    idle: _AwareDatetime
    """Date and time since which the user is idle on the session."""

    line: str | None = None
    """Line on which the user is connected to the session."""

    host: str | None = None
    """Host from which the user is connected on the line."""

    @_model_validator(mode="before")
    @classmethod
    def process_datetimes_at_model_creation(cls, data: _Any) -> _Any:
        """Process session start and idle date and times at model creation.

        This ensures the following rules:

        * :py:attr:`start`, if provided timezone-naive, should be coersced into
          a timezone-aware UTC datetime.
        * :py:attr:`idle`, if not provided, should be set to :py:attr:`start`.
          Note that if :py:attr:`start` is not or badly provided, no error
          should be reported for :py:attr:`idle` in this case.
        * :py:attr:`idle`, if provided timezone-naive, should be coersced into
          a timezone-aware UTC datetime.
        * If :py:attr:`idle` is before :py:attr:`start`, it should be coersced
          to :py:attr:`start`'s value.

        :param data: The raw model data to be processed.
        """
        if not isinstance(data, dict):
            return data

        start = data.get("start")
        if not isinstance(start, _datetime):
            # No error should be raised for :py:attr:`idle` if not provided.
            if "idle" not in data:
                data["idle"] = _datetime.min.replace(tzinfo=_timezone.utc)
            else:
                # Do not report a 'timezone missing' if idle is provided
                # as a timezone-naive datetime, since this would have been
                # coersced should start have been valid.
                idle = data["idle"]
                if isinstance(idle, _datetime) and idle.tzinfo is None:
                    data["idle"] = idle.replace(tzinfo=_timezone.utc)

            return data

        if start.tzinfo is None:
            _logger.info(
                "%s.start did not have a timezone, setting UTC",
                cls.__name__,
            )
            start = start.replace(tzinfo=_timezone.utc)

        if "idle" not in data:
            idle = start
        else:
            idle = data.get("idle")
            if isinstance(idle, _datetime):
                if idle.tzinfo is None:
                    _logger.info(
                        "%s.idle did not have a timezone, setting UTC",
                        cls.__name__,
                    )
                    idle = idle.replace(tzinfo=_timezone.utc)

                if idle < start:
                    _logger.warning(
                        "%s.idle (%s) was before %s.start (%s), coerscing",
                        cls.__name__,
                        idle.isoformat(),
                        cls.__name__,
                        start.isoformat(),
                    )
                    idle = start

        data["start"] = start
        data["idle"] = idle
        return data


class FingerUser(_BaseModel):
    """Representation of a user on the system.

    Such objects are returned by subclasses of :py:class:`FingerInterface`,
    and used by subclasses of :py:class:`FingerFormatter`.
    """

    model_config = _ConfigDict(strict=True, frozen=True)
    """Configuration dictionary for the model."""

    login: str | None = None
    """The login name of the user, e.g. ``cake`` or ``gaben``."""

    name: str | None = None
    """The display name of the user, e.g. ``Jean Dupont``."""

    office: str | None = None
    """The display name of the user's office."""

    plan: str | None = None
    """The user's plan.

    Usually the content of the ``.plan`` file in the user's home on real
    (and kind of obsolete) UNIX-like systems.
    """

    home: str | None = None
    """The path to the home directory of the user."""

    shell: str | None = None
    """The path to the user's default shell."""

    last_login: _AwareDatetime | None = None
    """The last login date and time for the user.

    If no such date and time is available, this property should be set to None.
    """

    sessions: list[FingerSession] = []
    """The user's current sessions."""

    @_field_validator("last_login", mode="before")
    @classmethod
    def add_utc_timezone_to_last_login(cls, value: _Any) -> _Any:
        """Add the UTC timezone if the last login date is timezone-naive."""
        if isinstance(value, _datetime) and value.tzinfo is None:
            value = value.replace(tzinfo=_timezone.utc)

        return value


class FingerFormatter:
    """Formatter for :py:class:`pyfingerd.server.FingerServer`.

    Provides text-formatted (as strings limited to ASCII)
    answers for given queries with given results as objects.

    This class must be subclassed by other formatters.
    Only methods not starting with an underscore are called by
    instances of :py:class:`pyfingerd.server.FingerServer`; others are
    utilities called by these.

    Unless methods are overridden to have a different behaviour,
    this formatter aims at RFC 1288 compliance.

    :param tzinfo: Timezone used for formatting dates and times.
    """

    __slots__ = ("_tzinfo",)

    def __init__(self, *, tzinfo: _tzinfo | None = None):
        if tzinfo is None:
            tzinfo = _datetime.now().astimezone().tzinfo

        self._tzinfo = tzinfo

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def _format_header(self, hostname: str, raw_query: str, /) -> str:
        """Return the header of the formatted answer.

        This header is used for every request,
        except when an error has occurred in the user's query.

        :param hostname: The hostname configured for the server.
        :param raw_query: The raw query given by the user.
        :return: The header of the formatted answer as text.
        """
        if raw_query:
            raw_query = " " + raw_query

        return (
            f"Site: {hostname}\r\n" + f"Command line:{raw_query}\r\n" + "\r\n"
        )

    def _format_footer(self, /) -> str:
        """Return the footer of the formatted answer.

        This footer is used for every request,
        except when an error has occurred in the user's query.

        :return: The footer of the formatted answer as text.
        """
        return ""

    def format_query_error(self, hostname: str, raw_query: str, /) -> str:
        """Return the formatted answr for when an error has occurred.

        :param hostname: The hostname configured for the server.
        :param raw_query: The raw query given by the user.
        :return: The formatted answer as text.
        """
        return (
            f"Site: {hostname}\r\n"
            + "You have made a mistake in your query!\r\n"
        )

    # ---
    # Short user list formatting.
    # ---

    def _format_short_login(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format a login for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        return user.login or ""

    def _format_short_name(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format a display name for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        return user.name or ""

    def _format_short_line(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format a line for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        if session is None:
            return ""
        return session.line or ""

    def _format_short_idle(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format an idle delta for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        if session is None:
            return ""

        delta = _datetime.utcnow().replace(tzinfo=_timezone.utc) - session.idle
        if delta < _timedelta():
            return ""

        days = int(delta.days)
        hours = int(delta.seconds / 3600)
        mins = int(delta.seconds % 3600 / 60)

        if days:
            return f"{days}d"
        if hours or mins:
            return f"{hours:02}:{mins:02}"

        return ""

    def _format_short_when(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format a start date and time for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        if session is None:
            return ""

        return session.start.astimezone(self._tzinfo).strftime("%a %H:%M")

    def _format_short_office(
        self,
        user: FingerUser,
        session: FingerSession | None,
        /,
    ) -> str:
        """Format an office for a session entry in short format.

        :param user: The user for the entry.
        :param session: The session for the entry.
        :return: The formatted column entry.
        """
        if session is None:
            return ""
        if session.host:
            return f"({session.host})"
        if user.office:
            return user.office
        return ""

    def format_short(
        self,
        hostname: str,
        raw_query: str,
        users: _Sequence[FingerUser],
        /,
    ) -> str:
        """Return the formatted answer for a user list in the 'short' format.

        :param hostname: The hostname configured for the server.
        :param raw_query: The raw query given by the user.
        :param users: The user list.
        :return: The formatted answer as text.
        """
        if not users:
            return "No user list available.\r\n"

        rows = [("Login", "Name", "TTY", "Idle", "When", "Office")]
        aligns = ("<", "<", "<", "^", "^", "<")

        for user in users:
            if not user.sessions:
                rows.append(
                    (
                        self._format_short_login(user, None),
                        self._format_short_name(user, None),
                        self._format_short_line(user, None),
                        self._format_short_idle(user, None),
                        self._format_short_when(user, None),
                        self._format_short_office(user, None),
                    ),
                )

            for session in user.sessions:
                rows.append(
                    (
                        self._format_short_login(user, session),
                        self._format_short_name(user, session),
                        self._format_short_line(user, session),
                        self._format_short_idle(user, session),
                        self._format_short_when(user, session),
                        self._format_short_office(user, session),
                    ),
                )

        sizes = tuple(
            max(len(row[i]) for row in rows) for i in range(len(rows[0]))
        )

        lines = []
        for row in rows:
            lines.append(
                " ".join(
                    f"{column[:size]:{align}{size + 1}}"
                    for column, align, size in zip(row, aligns, sizes)
                ),
            )

        return (
            self._format_header(hostname, raw_query)
            + "\r\n".join(lines)
            + "\r\n"
            + self._format_footer()
        )

    # ---
    # Long user list formatting.
    # ---

    def _format_long_idle(self, idle: _timedelta, /) -> str:
        """Format an idle time delta in long format.

        :param idle: The time delta to format.
        :return: The formatted time delta.
        """

        def _iter_idle(idle: _timedelta) -> _Iterator[str]:
            days = int(idle.days)
            hours = int(idle.seconds / 3600)
            mins = int(idle.seconds % 3600 / 60)
            secs = int(idle.seconds % 60)

            if days:
                yield f'{days} day{("", "s")[days > 1]}'
            if hours:
                yield f'{hours} hour{("", "s")[hours > 1]}'
            if mins:
                yield f'{mins} minute{("", "s")[mins > 1]}'
            if secs or (not days and not hours and not mins):
                # We want to be able to display "0 seconds" if necessary.
                yield f'{secs} second{("", "s")[secs > 1]}'

        return f'{" ".join(_iter_idle(idle))} idle'

    def format_long(
        self,
        hostname: str,
        raw_query: str,
        users: _Sequence[FingerUser],
    ) -> str:
        """Return the formatted answer for a user list in the 'long' format.

        :param hostname: The hostname configured for the server.
        :param raw_query: The raw query given by the user.
        :param users: The user list.
        :return: The formatted answer as text.
        """
        if not users:
            return "No user list available.\r\n"

        now = _datetime.now().astimezone()
        result = ""

        for user in users:
            result += (
                f'Login name: {user.login or "":<27.27} '
                + f'Name: {user.name if user.name else user.login or ""}\r\n'
                + f'Directory: {user.home if user.home else "":<28.28} '
                + f'Shell: {user.shell if user.shell else ""}\r\n'
            )
            if user.office:
                result += f'Office: {user.office if user.office else ""}\r\n'

            if user.sessions:
                # List current sessions.
                for session in user.sessions:
                    since = session.start.astimezone(self._tzinfo).strftime(
                        "%a %b %e %R",
                    )

                    tzinfo = self._tzinfo
                    result += f"On since {since} ({tzinfo})"
                    if session.line is not None:
                        result += f" on {session.line}"
                    if session.host is not None:
                        result += f" from {session.host}"
                    result += "\r\n"

                    idle = now - session.idle
                    if idle >= _timedelta(seconds=4):
                        result += f"   {self._format_long_idle(idle)}\r\n"
            elif user.last_login is not None:
                # Show last login.
                date = user.last_login.astimezone(self._tzinfo).strftime(
                    "%a %b %e %R",
                )
                tzinfo = self._tzinfo
                result += f"Last login {date} ({tzinfo}) on console\r\n"
            else:
                result += "Never logged in.\r\n"

            if user.plan is None:
                result += "No plan.\r\n"
            else:
                result += "Plan:\r\n"
                result += "\r\n".join(user.plan.splitlines())
                result += "\r\n"

            result += "\r\n"

        return (
            self._format_header(hostname, raw_query)
            + result
            + self._format_footer()
        )


class FingerInterface:
    """Data source for :py:class:`pyfingerd.server.FingerServer`.

    Provides users and answers for the various queries received
    from the clients by the server.

    This class must be subclassed by other interfaces.
    Only methods not starting with an underscore are called by
    instances of :py:class:`pyfingerd.server.FingerServer`; others are
    utilities called by these.

    By default, it behaves like a dummy interface.
    """

    __slots__ = ()

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def transmit_query(
        self,
        query: str | None,
        host: str,
        verbose: bool,
    ) -> str:
        """Transmit a user query to a foreign host.

        This function returns the answer formatted by it.

        If used directly (not overridden by subclasses), this
        method will refuse to transmit finger queries.

        :param query: The user query, set to None in case of
                      no query provided by the client.
        :param host: The distant host to which to transmit the query.
        :param verbose: Whether the verbose flag (``/W``, long format)
                        has been passed by the current client or not.
        :return: The answer formatted by the distant server.
        """
        return "This server won't transmit finger queries.\r\n"

    def search_users(
        self,
        query: str | None,
        active: bool | None,
    ) -> _Sequence[FingerUser]:
        """Search for users on the current host using the given query.

        :param query: The user query, set to None in case of no
                      query provided by the client.
        :param active: Whether to get active users (True),
                       inactive users (False), or all users (None).
        :return: The list of users found using the query provided
                 by the client.
        """
        return []
