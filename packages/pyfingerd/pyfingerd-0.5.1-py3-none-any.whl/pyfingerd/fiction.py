#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Definitions for the finger server fiction interface.

This file contains everything to decode and use the actions file.
"""

from __future__ import annotations

from collections import defaultdict as _defaultdict
from collections.abc import (
    Iterable as _Iterable,
    Iterator as _Iterator,
    Sequence as _Sequence,
)
import copy as _copy
from datetime import (
    datetime as _datetime,
    timedelta as _timedelta,
    timezone as _timezone,
)
from enum import Enum as _Enum
from itertools import chain as _chain
import logging as _logging
import math as _math
from pathlib import Path as _Path
from sys import exit as _sys_exit
from typing import Any as _Any, TypeVar as _TypeVar

from pydantic import (
    BaseModel as _BaseModel,
    ConfigDict as _ConfigDict,
    NaiveDatetime as _NaiveDatetime,
)
from toml import load as _load_toml

from .core import (
    FingerInterface as _FingerInterface,
    FingerSession as _FingerSession,
    FingerUser as _FingerUser,
    cron as _cron,
)
from .utils import (
    Unchanged as _Unchanged,
    UnchangedType as _UnchangedType,
    format_delta as _format_delta,
    logger as _logger,
    make_delta as _make_delta,
    parse_delta as _parse_delta,
)


__all__ = [
    "FictionalSession",
    "FictionalUser",
    "FingerAction",
    "FingerFictionInterface",
    "FingerScenario",
    "FingerScenarioInterface",
    "FingerUserCreationAction",
    "FingerUserDeletionAction",
    "FingerUserEditionAction",
    "FingerUserLoginAction",
    "FingerUserLogoutAction",
    "FingerUserSessionChangeAction",
]

_FingerScenarioType = _TypeVar("_FingerScenarioType", bound="FingerScenario")

# ---
# Fiction state.
# ---


class FictionalSession(_BaseModel):
    """Representation of an active session for a given user."""

    model_config = _ConfigDict(strict=True, validate_assignment=True)
    """Configuration dictionary for the model."""

    start: _NaiveDatetime
    """The creation date and time for the session, UTC-based."""

    line: str | None = None
    """Equivalent attribute to :py:attr:`FingerSession.line`."""

    host: str | None = None
    """Equivalent attribute to :py:attr:`FingerSession.host`."""

    is_idle: bool
    """Whether the user is currently idle on the session, or not."""

    last_idle_event: _NaiveDatetime
    """The date and time of the last idle event, UTC-based."""


class FictionalUser(_BaseModel):
    """Representation of a user on the fictional system.

    This will be used to produce :py:class:`FingerUser` instances by
    :py:meth:`FingerFictionInterface.search_users`.
    """

    model_config = _ConfigDict(strict=True, validate_assignment=True)
    """Configuration dictionary for the model."""

    name: str | None = None
    """Equivalent attribute to :py:attr:`FingerUser.name`."""

    office: str | None = None
    """Equivalent attribute to :py:attr:`FingerUser.office`."""

    plan: str | None = None
    """Equivalent attribute to :py:attr:`FingerUser.plan`."""

    home: str | None = None
    """Equivalent attribute to :py:attr:`FingerUser.home`."""

    shell: str | None = None
    """Equivalent attribute to :py:attr:`FingerUser.shell`."""

    last_login: _NaiveDatetime | None = None
    """Equivalent attribute to :py:attr:`FingerUser.last_login`.

    This property will be placed into the UTC timezone before producing
    a :py:class:`FingerUser`.
    """

    unnamed_sessions: list[FictionalSession] = []
    """Current unnamed sessions for the user."""

    named_sessions: dict[str, FictionalSession] = {}
    """Current named sessions for the user."""


# ---
# Actions and fiction definition.
# ---


class FingerAction(_BaseModel):
    """Base class for actions in a fiction."""

    model_config = _ConfigDict(
        strict=True,
        frozen=True,
        arbitrary_types_allowed=True,  # Required for using Unchanged.
    )
    """Configuration dictionary for the model."""


class FingerUserCreationAction(FingerAction):
    """A user has been created."""

    login: str
    """The login of the user to create."""

    name: str | None = None
    """The value for :py:attr:`FictionalUser.name` on the new object."""

    home: str | None = None
    """The value for :py:attr:`FictionalUser.home` on the new object."""

    shell: str | None = None
    """The value for :py:attr:`FictionalUser.shell` on the new object."""

    office: str | None = None
    """The value for :py:attr:`FictionalUser.office` on the new object."""

    plan: str | None = None
    """The value for :py:attr:`FictionalUser.plan` on the new object."""


class FingerUserEditionAction(FingerAction):
    """A user has been edited."""

    login: str
    """The login of the user to edit."""

    name: str | None | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalUser.name`."""

    home: str | None | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalUser.home`."""

    shell: str | None | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalUser.shell`."""

    office: str | None | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalUser.office`."""

    plan: str | None | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalUser.plan`."""


class FingerUserDeletionAction(FingerAction):
    """A user has been deleted."""

    login: str
    """The login of the user to delete."""


class FingerUserLoginAction(FingerAction):
    """A user has logged in."""

    login: str
    """The login of the user for which to create a session."""

    session_name: str | None = None
    """The name of the session to create."""

    line: str | None = None
    """The value for :py:attr:`FictionalSession.line` on the new object."""

    host: str | None = None
    """The value for :py:attr:`FictionalSession.host` on the new object."""


class FingerUserSessionChangeAction(FingerAction):
    """A user session has undergone modifications."""

    login: str
    """The login of the user for which to change the session."""

    session_name: str | None = None
    """The name of the session to change for the user."""

    idle: bool | _UnchangedType = _Unchanged
    """The new value for :py:attr:`FictionalSession.is_idle`."""


class FingerUserLogoutAction(FingerAction):
    """A user has logged out."""

    login: str
    """The login of the user for which to destroy a session."""

    session_name: str | None = None
    """The name of the session to destroy."""


class FingerScenario:
    """Scenario representation for the fictional interface.

    Consists of actions (as instances of subclasses of
    :py:class:`FingerAction`) located at a given timedelta, with
    a given ending type and time.

    A scenario always uses timedeltas and not datetimes, since it can
    start at any arbitrary point in time and some scenarios are even
    on repeat.
    """

    __slots__ = ("_end_type", "_end_time", "_actions")

    class EndingType(_Enum):
        """Ending type, i.e. what happens when the scenario comes to an end."""

        FREEZE = 0
        """Freeze the end state forever."""

        STOP = 1
        """Stop the server as soon as the scenario has reached an end."""

        REPEAT = 2
        """Repeat the scenario from the beginning while starting again from
        the initial state.
        """

    _end_type: FingerScenario.EndingType
    _end_time: _timedelta
    _actions: list[tuple[_timedelta, FingerAction, int]]

    @property
    def ending_type(self) -> FingerScenario.EndingType:
        """Get the ending type of the scenario."""
        return self._end_type

    @property
    def duration(self) -> _timedelta:
        """Offset of the ending.

        When the offset is reached, any object following
        the scenario should act out the ending type defined
        in :py:attr:`ending_type`.
        """
        return self._end_time

    def __init__(
        self,
        *,
        ending_type: FingerScenario.EndingType | str = EndingType.FREEZE,
        duration: _timedelta | str,
    ):
        if isinstance(ending_type, str):
            try:
                ending_type = {
                    "interrupt": self.EndingType.FREEZE,
                    "freeze": self.EndingType.FREEZE,
                    "stop": self.EndingType.STOP,
                    "repeat": self.EndingType.REPEAT,
                }[ending_type.casefold()]
            except KeyError as exc:
                raise TypeError(
                    f"Invalid value for ending type: {ending_type!r}",
                ) from exc

        self._end_type = ending_type
        self._end_time = _make_delta(duration)
        self._actions = []

    @classmethod
    def load(cls: type[_FingerScenarioType], path: str) -> _FingerScenarioType:
        """Load a scenario from a TOML file.

        Decodes the content of a scenario in TOML format and, if
        successful, returns the result as an instance of FingerScenario.

        :param path: Path of the TOML file to load.
        """
        actions = []
        end_type = None
        end_time = None

        _logger.debug("Loading scenario from %r.", path)

        # Read the document and translate all of the timestamps.
        document = _load_toml(path)
        i = 0

        for key in document.keys():
            time = _parse_delta(key)
            if time is None:
                raise ValueError(f"Found invalid time: {key!r}")

            if not isinstance(document[key], list):
                raise ValueError(
                    f"Time {key!r} is not an array, "
                    + f"you have probably written [{key}] instead of "
                    + f"[[{key}]]",
                )

            for j, data in enumerate(document[key]):
                try:
                    typ = data["type"]
                    if typ in ("interrupt", "freeze", "stop", "repeat"):
                        # Set the ending type and time.
                        if end_time is None or end_time > time:
                            end_type = {
                                "interrupt": cls.EndingType.FREEZE,
                                "freeze": cls.EndingType.FREEZE,
                                "stop": cls.EndingType.STOP,
                                "repeat": cls.EndingType.REPEAT,
                            }[typ]
                            end_time = time

                        continue

                    action: FingerAction
                    plan: str | None | _UnchangedType
                    if typ == "create":
                        # User creation.
                        plan = None
                        if "plan" in data:
                            with open(
                                _Path(path).parent / data["plan"],
                                encoding="ascii",
                                errors="ignore",
                            ) as plan_file:
                                plan = plan_file.read()

                        action = FingerUserCreationAction(
                            login=data["login"],
                            name=data.get("name"),
                            shell=data.get("shell"),  # NOQA
                            home=data.get("home"),
                            office=data.get("office"),
                            plan=plan,
                        )
                    elif typ == "update":
                        # User update.
                        plan = _Unchanged
                        if "plan" in data:
                            if data["plan"] is False:
                                plan = None
                            else:
                                with open(
                                    _Path(path).parent / data["plan"],
                                    encoding="ascii",
                                    errors="ignore",
                                ) as plan_file:
                                    plan = plan_file.read()

                        def coersce_from_key(
                            key: str,
                            /,
                        ) -> str | None | _UnchangedType:
                            """Coersce a key to a value, None or Unchanged."""
                            if key in data and data[key] is False:
                                return None

                            return data.get(key, _Unchanged)

                        action = FingerUserEditionAction(
                            login=data["login"],
                            name=coersce_from_key("name"),
                            shell=coersce_from_key("shell"),  # NOQA
                            home=coersce_from_key("home"),
                            office=coersce_from_key("office"),
                            plan=plan,
                        )
                    elif typ == "delete":
                        # User deletion.
                        action = FingerUserDeletionAction(login=data["login"])
                    elif typ == "login":
                        # User login.
                        action = FingerUserLoginAction(
                            login=data["login"],
                            session_name=data.get("session"),
                            line=data.get("line"),
                            host=data.get("host"),
                        )
                    elif typ == "logout":
                        # User logout.
                        action = FingerUserLogoutAction(
                            login=data["login"],
                            session_name=data.get("session"),
                        )
                    elif typ in ("idle", "active"):
                        # Idle change status.
                        action = FingerUserSessionChangeAction(
                            login=data["login"],
                            session_name=data.get("session"),
                            idle=(typ == "idle"),
                        )
                    else:
                        raise ValueError(f"Invalid action type {typ!r}")

                    actions.append((time, action, i))
                    i += 1
                except Exception as exc:
                    msg = str(exc)
                    msg = msg[0].lower() + msg[1:]
                    raise ValueError(
                        f"At action #{j + 1} at {_format_delta(time)}: {msg}",
                    ) from None

        # Sort and check the actions.
        _logger.debug(
            "Loaded %d action%s.",
            len(actions),
            "s"[: len(actions) >= 2],
        )

        if end_type is None:
            # If no ending was given in the script file, we ought to
            # interrupt 10 seconds after the last action.
            try:
                last_time = max(actions, key=lambda x: (x[0], x[2]))[0]
            except ValueError:
                last_time = _timedelta(seconds=0)

            end_type = cls.EndingType.FREEZE

        if end_time is None:
            end_time = last_time + _timedelta(seconds=10)

        scenario = cls(ending_type=end_type, duration=end_time)
        for time, action, *_ in actions:
            scenario.add(action, time)

        return scenario

    def verify(self) -> None:
        """Verify that the current scenario is valid.

        This function does the following checks on the scenario:

        * The ending type and time (duration) are well defined.
        * Any user edition or deletion event happens when the
          related user exists.
        * Any session creation, edition or deletion happens on
          a user who exists at that point in time.
        * Any session edition or deletion happens when the
          related session exists.

        Any action defined after the ending time is ignored.

        :raise ValueError: whether the current scenario is invalid.
        """
        users: set[str] = set()
        named_sessions: _defaultdict[str, set[str]] = _defaultdict(set)
        unnamed_sessions: _defaultdict[str, int] = _defaultdict(lambda: 0)

        for time, action, i in self._actions:
            try:
                if time >= self._end_time:
                    # Action will be ignored.
                    pass
                elif isinstance(action, FingerUserCreationAction):
                    if action.login in users:
                        # The user we're trying to create already exists.
                        raise ValueError(
                            "Trying to create user "
                            + f'"{action.login}" which already exists',
                        )

                    users.add(action.login)
                elif isinstance(action, FingerUserEditionAction):
                    if action.login not in users:
                        # The user we're trying to edit doesn't exist.
                        raise ValueError(
                            "Trying to edit user "
                            + f'"{action.login}" while it doesn\'t exist',
                        )
                elif isinstance(action, FingerUserDeletionAction):
                    if action.login not in users:
                        # The user we're trying to delete doesn't exist.
                        raise ValueError(
                            "Trying to delete user "
                            + f'"{action.login}" while it doesn\'t exist',
                        )

                    users.remove(action.login)
                    if action.login in named_sessions:
                        del named_sessions[action.login]
                    if action.login in unnamed_sessions:
                        del unnamed_sessions[action.login]
                elif isinstance(action, FingerUserLoginAction):
                    if action.login not in users:
                        # The user we're trying to log in as doesn't exist.
                        raise ValueError(
                            "Trying to log in as user "
                            + f'"{action.login}" which doesn\'t exist',
                        )

                    if action.session_name is not None:
                        if action.session_name in named_sessions[action.login]:
                            raise ValueError(
                                "Trying to log in with already taken "
                                + f'session name "{action.session_name}" '
                                + f'for user "{action.login}"',
                            )

                        named_sessions[action.login].add(action.session_name)
                    else:
                        unnamed_sessions[action.login] += 1
                elif isinstance(action, FingerUserSessionChangeAction):
                    if action.login not in users:
                        raise ValueError(
                            "Trying to update session of non existing "
                            + f'user "{action.login}"',
                        )

                    if action.session_name is not None:
                        if (
                            action.session_name
                            not in named_sessions[action.login]
                        ):
                            raise ValueError(
                                "Trying to update non-existing named "
                                + f'session "{action.session_name}" of '
                                + f'user "{action.login}"',
                            )
                    elif unnamed_sessions[action.login] <= 0:
                        raise ValueError(
                            "Trying to change unprovisioned unnamed session "
                            + f'of user "{action.login}"',
                        )
                elif isinstance(action, FingerUserLogoutAction):
                    if action.login not in users:
                        raise ValueError(
                            "Trying to delete session of non-existing "
                            + f'user "{action.login}"',
                        )

                    if action.session_name is not None:
                        if (
                            action.session_name
                            not in named_sessions[action.login]
                        ):
                            raise ValueError(
                                "Trying to delete non-existing named "
                                + f'session "{action.session_name}" of '
                                + f'user "{action.login}"',
                            )

                        named_sessions[action.login].remove(
                            action.session_name,
                        )
                    else:
                        if unnamed_sessions[action.login] <= 0:
                            raise ValueError(
                                "Trying to delete unprovisioned unnamed "
                                + f'session of user "{action.login}"',
                            )

                        unnamed_sessions[action.login] -= 1
            except ValueError as exc:
                msg = str(exc)
                msg = msg[0].lower() + msg[1:]
                raise ValueError(
                    f"At action #{i} at {_format_delta(time)}: {msg}",
                ) from None

    def get(
        self,
        *,
        until: _timedelta | None = None,
        since: _timedelta | None = None,
    ) -> _Iterator[tuple[_timedelta, FingerAction]]:
        """Return a sequence of actions in order from the scenario.

        :param until: Maximum timedelta for the actions to gather.
        :param since: Minimum timedelta for the actions to gather.
        :return: The sequence of actions that occur and respect
            the given constraints.
        """
        if since is not None and until is not None and since > until:
            raise ValueError(
                f"`since` ({since}) should be before `until` ({until}).",
            )

        for time, action, _ in self._actions:
            if since is not None and since >= time:
                continue
            if until is not None and time > until:
                continue
            if self._end_time is not None and time >= self._end_time:
                continue
            yield time, action

    def add(self, action: FingerAction, time: _timedelta | str) -> None:
        """Add an action at the given time to the registered actions."""
        time = _make_delta(time)

        try:
            index = max(x[2] for x in self._actions)
        except ValueError:
            index = 0

        self._actions.append((time, action, index + 1))
        self._actions.sort(key=lambda x: (x[0], x[2]))


# ---
# Interfaces.
# ---


class FingerFictionInterface(_FingerInterface):
    """Base finger fiction interface for managing a scene.

    The basic state for this class is to have no users; it is possible
    at any point in time to apply actions that will add, remove or
    modify users and sessions, using
    :py:meth:`FingerFictionInterface.apply`.

    This class should be subclassed for interfaces specialized in various
    sources for the data; for example, while
    :py:class:`FingerScenarioInterface` is specialized in using a
    static sequence of actions, another class could read events from
    a live source.
    """

    __slots__ = ("_users", "_lasttime")

    _users: dict[str, FictionalUser]
    """Current state of the fiction, indexed by login."""

    _lasttime: _datetime | None
    """The last date and time of application of actions.

    This allows us to raise an exception if actions are not applied in
    order, as a simple integrity check.
    """

    def __init__(self):
        super().__init__()

        self._users = {}
        self._lasttime = None

    # ---
    # Expected methods from an interface.
    # ---

    def search_users(
        self,
        query: str | None,
        active: bool | None,
    ) -> _Sequence[_FingerUser]:
        """Look for users according to a check."""
        users = []
        now = _datetime.utcnow()
        for login, fictional_user in self._users.items():
            if query is not None and query not in login:
                continue

            if (
                active is True
                and not fictional_user.named_sessions
                and not fictional_user.unnamed_sessions
            ):
                continue

            if active is False and (
                fictional_user.named_sessions
                or fictional_user.unnamed_sessions
            ):
                continue

            sessions: list[_FingerSession] = []
            for fictional_session in _chain(
                fictional_user.named_sessions.values(),
                fictional_user.unnamed_sessions,
            ):
                if fictional_session.is_idle is not None:
                    idle = fictional_session.last_idle_event
                else:
                    seconds = (now - fictional_session.last_idle_event).seconds
                    random_seconds = int(
                        abs(_math.sin(seconds * (_math.pi / 2)))
                        + abs(_math.sin(seconds / 4 * (_math.pi / 2))),
                    )

                    idle = now - _timedelta(seconds=random_seconds)

                start = fictional_session.start.replace(tzinfo=_timezone.utc)
                sessions.append(
                    _FingerSession(
                        start=start,
                        idle=idle.replace(tzinfo=_timezone.utc),
                        line=fictional_session.line,
                        host=fictional_session.host,
                    ),
                )

            last_login = fictional_user.last_login
            if last_login is not None:
                last_login = last_login.replace(tzinfo=_timezone.utc)

            users.append(
                _FingerUser(
                    login=login,
                    name=fictional_user.name,
                    office=fictional_user.office,
                    plan=fictional_user.plan,
                    home=fictional_user.home,
                    shell=fictional_user.shell,  # noqa: S604
                    last_login=last_login,
                    sessions=tuple(sessions),
                ),
            )

        return users

    # ---
    # Elements proper to the fiction interface.
    # ---

    def reset(self) -> None:
        """Reset the interface, i.e. revert all actions.

        This method makes the interface return to the original
        state with no users and sessions.
        """
        self._users = {}
        self._lasttime = None

    def apply(
        self,
        action: FingerAction,
        time: _datetime | None = None,
    ) -> None:
        """Apply an action to the scene.

        By default, the time of the action is the current time.
        """
        if time is None:
            time = _datetime.utcnow()
        if time.tzinfo is not None:
            time = time.astimezone(_timezone.utc).replace(tzinfo=None)

        if self._lasttime is not None and self._lasttime > time:
            raise ValueError("Operations weren't applied in order!")

        self._lasttime = time

        if isinstance(action, FingerUserCreationAction):
            # Create user `action.user`.
            if action.login is None:
                raise ValueError("Missing login")
            if action.login in self._users:
                raise ValueError("Already got a user with that login")

            self._users[action.login] = FictionalUser(
                login=action.login,
                name=action.name,
                shell=action.shell,  # noqa: S604
                home=action.home,
                office=action.office,
                plan=action.plan,
            )
        elif isinstance(action, FingerUserEditionAction):
            # Edit user `action.user` with the given modifications.
            if action.login is None:
                raise ValueError("Missing login")
            if action.login not in self._users:
                raise ValueError(
                    f"Got no user with login {action.login!r}",
                )

            user = self._users[action.login]
            if not isinstance(action.name, _UnchangedType):
                user.name = action.name
            if not isinstance(action.shell, _UnchangedType):
                user.shell = action.shell
            if not isinstance(action.home, _UnchangedType):
                user.home = action.home
            if not isinstance(action.office, _UnchangedType):
                user.office = action.office
            if not isinstance(action.plan, _UnchangedType):
                user.plan = action.plan
        elif isinstance(action, FingerUserDeletionAction):
            # Delete user with login `action.login`.
            if action.login is None:
                raise ValueError("Missing login")
            if action.login not in self._users:
                raise ValueError(
                    f"Got no user with login {action.login!r}",
                )

            del self._users[action.login]
        elif isinstance(action, FingerUserLoginAction):
            # Login as user `action.login` with session `action.session_name`.
            session = FictionalSession(
                start=time,
                line=action.line,
                host=action.host,
                is_idle=False,
                last_idle_event=time,
            )

            if action.login is None:
                raise ValueError("Missing login")

            try:
                user = self._users[action.login]
            except KeyError:
                raise ValueError(
                    f"Got no user with login {action.login!r}",
                ) from None

            # We don't check if the session exists or not; multiple
            # sessions can have the same name, we just act on the last
            # inserted one that still exists and has that name.
            if action.session_name:
                if action.session_name in user.sessions:
                    raise ValueError(
                        "Session already exists for user with login "
                        + f"{action.login!r} and name {action.session_name!r}",
                    )

                user.named_sessions[action.session_name] = session
            else:
                user.unnamed_sessions.append(session)

            if user.last_login is None or user.last_login < session.start:
                user.last_login = session.start
        elif isinstance(action, FingerUserLogoutAction):
            # Logout as user `action.login` from
            # session `action.session_name`.
            if action.login is None:
                raise ValueError("Missing login")

            try:
                user = self._users[action.login]
            except KeyError:
                raise ValueError(
                    f"Got no user with login {action.login!r}",
                ) from None

            if action.session_name:
                try:
                    del user.named_sessions[action.session_name]
                except (KeyError, IndexError):
                    raise ValueError(
                        f"Got no session named {action.session_name!r} "
                        + f"for user with login {action.login!r}",
                    ) from None
            else:
                try:
                    user.unnamed_sessions.pop(-1)
                except IndexError:
                    raise ValueError(
                        "No unnamed sessions left for user with "
                        + f"login {action.login!r}",
                    ) from None
        elif isinstance(action, FingerUserSessionChangeAction):
            # Make user with login `action.login` idle.
            if action.login is None:
                raise ValueError("Missing login")

            try:
                user = self._users[action.login]
            except KeyError:
                raise ValueError(
                    f"Got no user with login {action.login!r}",
                ) from None

            if action.session_name is not None:
                try:
                    user_session = user.named_sessions[action.session_name]
                except KeyError:
                    raise ValueError(
                        f"Got no session {action.session_name!r} "
                        + f"for user {action.login!r}",
                    ) from None
            else:
                try:
                    user_session = user.unnamed_sessions[-1]
                except IndexError as exc:
                    raise ValueError(
                        f"Got no unnamed session for user {action.login!r}",
                    ) from exc

            session = user_session
            if isinstance(action.idle, _UnchangedType):
                pass
            elif action.idle != session.is_idle:
                session.last_idle_event = time
                session.is_idle = action.idle


class FingerScenarioInterface(FingerFictionInterface):
    """Fiction interface, to follow actions written in a scenario.

    Subclasses :py:class:`FingerFictionInterface` and adds
    a regular update method for updating the state according
    to the given scenario.

    :param scenario: The scenario to follow using the given interface.
    :param start: The start time at which the scenario is supposed to
        have started; by default, the current time is used.
    """

    __slots__ = ("_scenario", "_start", "_laststart", "_lastdelta")

    _scenario: FingerScenario
    """The scenario to follow."""

    _start: _datetime
    """The starting date and time, as determined at class instantiation."""

    _laststart: _datetime | None
    """The last registered start.

    This may be different from :py:attr:`_start` when the scenario loops.
    """

    _lastdelta: _timedelta | None
    """The last registered delta.

    This is to determine at which duration the scenario was last refreshed.
    """

    def __init__(
        self,
        scenario: FingerScenario,
        start: _datetime | None = None,
    ):
        if start is None:
            start = _datetime.now()
        if start.tzinfo is None:
            start = start.astimezone()

        super().__init__()

        # Initialize the object properties.
        if not isinstance(scenario, FingerScenario):
            raise TypeError(
                "Scenario should be a FingerScenario, "
                + f"is {scenario.__class__.__name__}.",
            )

        scenario.verify()
        scenario = _copy.copy(scenario)

        # Initialize the object properties.
        # - `scenario`: the script to follow.
        # - `laststart`: the last registered start.
        # - `lastdelta`: the last registered delta.
        self._scenario = scenario
        self._start = start
        self._laststart = None
        self._lastdelta = None

    def _log_applied_actions(self, actions: list[FingerAction], /) -> None:
        """Log actions that are about to be applied.

        :param actions: The actions to log.
        """
        action_messages: list[str] = []
        log_args: list[_Any] = []
        for time, action in actions:
            properties: list[tuple[str, str | None]] = []
            if isinstance(action, FingerUserCreationAction):
                properties.append(("type", "create"))
                properties.append(("login", action.login))
                if action.name is not None:
                    properties.append(("name", action.name))
                if action.home is not None:
                    properties.append(("home", action.home))
                if action.shell is not None:
                    properties.append(("shell", action.shell))
                if action.office is not None:
                    properties.append(("office", action.office))
                if action.plan is not None:
                    properties.append(
                        (
                            "plan",
                            "\n    " + "\n    ".join(action.plan),
                        ),
                    )
            elif isinstance(action, FingerUserEditionAction):
                properties.append(("type", "update"))
                properties.append(("login", action.login))
                if not isinstance(action.name, _UnchangedType):
                    properties.append(("name", action.name))
                if not isinstance(action.home, _UnchangedType):
                    properties.append(("home", action.home))
                if not isinstance(action.shell, _UnchangedType):
                    properties.append(("shell", action.shell))
                if not isinstance(action.office, _UnchangedType):
                    properties.append(("office", action.office))
                if action.plan is None:
                    properties.append(("plan", action.plan))
                elif not isinstance(action.plan, _UnchangedType):
                    properties.append(
                        (
                            "plan",
                            "\n    " + "\n    ".join(action.plan),
                        ),
                    )
            elif isinstance(action, FingerUserDeletionAction):
                properties.append(("type", "delete"))
                properties.append(("login", action.login))
            elif isinstance(action, FingerUserLoginAction):
                properties.append(("type", "login"))
                properties.append(("login", action.login))
                if action.session_name is not None:
                    properties.append(
                        (
                            "session_name",
                            action.session_name,
                        ),
                    )
                if action.line is not None:
                    properties.append(("line", action.line))
                if action.host is not None:
                    properties.append(("host", action.host))
            elif isinstance(action, FingerUserSessionChangeAction):
                if action.idle:
                    properties.append(("type", "idle"))
                else:
                    properties.append(("type", "active"))

                properties.append(("login", action.login))
                if action.session_name is not None:
                    properties.append(
                        (
                            "session_name",
                            action.session_name,
                        ),
                    )
            elif isinstance(action, FingerUserLogoutAction):
                properties.append(("type", "logout"))
                properties.append(("login", action.login))
                if action.session_name is not None:
                    properties.append(
                        (
                            "session_name",
                            action.session_name,
                        ),
                    )
            else:
                properties.append(("type", "(unknown)"))

            action_messages.append(
                "At %s:\n" + "\n".join("  %s: %s" for _ in properties),
            )
            log_args += [_format_delta(time)]
            for key, value in properties:
                log_args.append(key)
                log_args.append(value if value is not None else "(none)")

        _logger.info(
            "Applying %d action%s:\n" + "\n\n".join(action_messages),
            len(actions),
            "s"[: len(actions) >= 2],
            *log_args,
        )

    @_cron("* * * * * *")
    def update(self) -> None:
        """Update the state according to the scenario every second."""
        now = _datetime.now().astimezone()
        start = self._laststart or self._start

        # Check if we have gone back in time, e.g. if the system time
        # has changed, and just start again.
        if self._lastdelta is not None and now < start + self._lastdelta:
            _logger.debug("We seem to have gone back in time!")
            _logger.debug("Let's start again from a clean slate.")

            start = self._start

            self._lastdelta = None
            self.reset()

        # Check if we have reached an ending.
        if now > start + self._scenario.duration:
            ending_type = self._scenario.ending_type
            if ending_type is None:
                raise AssertionError("Ending type shouldn't be None here!")

            if ending_type == FingerScenario.EndingType.STOP:
                _logger.debug("Stop ending has been reached.")
                _sys_exit()
            elif ending_type == FingerScenario.EndingType.FREEZE:
                delta = self._scenario.duration
            else:
                # We're on 'repeat', so we are going to have a slightly
                # different start because we want the start of the new
                # iteration.
                #
                #     >>> from datetime import (datetime as dt
                #         timedelta as td)
                #     >>> a = dt(2000, 1, 1)
                #     >>> b = a + td(seconds = 27)
                #     >>> (b - a) % td(seconds = 10)
                #     datetime.timedelta(seconds=7)
                #     >>> b - (b - a) % td(seconds = 10)
                #     datetime.datetime(2000, 1, 1, 0, 0, 20)
                #
                # Let's see.
                start = now - (now - start) % self._scenario.duration

                self.reset()
                self._lastdelta = None

                _logger.debug("Repeat ending has been reached.")
                _logger.debug("Looping from %s.", start.isoformat())

        # We're within the duration of the fiction, so we just use the
        # offset from the start.
        delta = now - start

        # Then, we apply the actions up to the current time.
        actions: _Iterable[
            tuple[_timedelta, FingerAction]
        ] = self._scenario.get(until=delta, since=self._lastdelta)

        if _logger.getEffectiveLevel() <= _logging.INFO:
            actions = list(actions)
            if actions:
                self._log_applied_actions(actions)  # type: ignore

        for time, action in actions:
            self.apply(action, start + time)

        # Finally, we can keep track of where we were.
        self._laststart = start
        self._lastdelta = delta
