#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd Python 3.x module, which is MIT-licensed.
# *****************************************************************************
"""Make use of the utmp/x file to read the user data.

This module can only load on POSIX compliant environments.
Importing it from other environments will result in an
:py:exc:`python:ImportError`.
"""

from __future__ import annotations

from collections import defaultdict as _defaultdict
from datetime import datetime as _datetime, timezone as _timezone
from multiprocessing import Lock as _Lock
from os import stat as _stat
from pathlib import Path as _Path
import pwd as _pwd

import pyutmpx as _pyutmpx

from .core import (
    FingerInterface as _FingerInterface,
    FingerSession as _FingerSession,
    FingerUser as _FingerUser,
)


__all__ = ["FingerPOSIXInterface"]


class FingerPOSIXInterface(_FingerInterface):
    """Finger interface for POSIX-compliant systems.

    The method for gathering users and sessions on such systems
    is the following:

    #. Get the users in ``/etc/passwd``, and check which ones not
       to make appear through the presence of ``.nofinger``
       in their home directory.
    #. Get the last login times for all users to display them
       by default, through the lastlog database if available.
    #. Get the sessions in the utmp / utmpx database, and make
       them correspond to the related user.
    #. For each session, get the idle time by gathering the
       mtime of the device.
    """

    __slots__ = ("_data", "_lastrefreshtime", "_lock")

    def __init__(self):
        self._data = []
        self._lastrefreshtime = None
        self._lock = _Lock()

    def search_users(
        self,
        query: str | None,
        active: bool | None,
    ) -> tuple[_FingerUser, ...]:
        """Look for users on POSIX-compliant systems.

        :param query: The user query.
        :param active: Whether to look for active users or not.
        :return: The result.
        """
        self._lock.acquire()

        try:
            # Refresh the user list if required.
            if (
                self._lastrefreshtime is None
                or abs(
                    (
                        self._lastrefreshtime - _datetime.utcnow()
                    ).total_seconds(),
                )
                >= 1
            ):
                lastlog_by_user_id: dict[int, _datetime] = {}
                sessions_by_user_login: _defaultdict[
                    str,
                    list[_FingerSession],
                ] = _defaultdict(list)

                try:
                    lastlog = _pyutmpx.lastlog
                except AttributeError:
                    pass
                else:
                    for lle in lastlog:
                        lastlog_by_user_id[lle.uid] = lle.time

                try:
                    utmp = _pyutmpx.utmp
                except AttributeError:
                    pass
                else:
                    for utmp_entry in utmp:
                        if utmp_entry.type != _pyutmpx.USER_PROCESS:
                            continue

                        start: _datetime = utmp_entry.time
                        if start.tzinfo is None:
                            start = start.replace(tzinfo=_timezone.utc)

                        idle = _datetime.utcnow()
                        if utmp_entry.line and not utmp_entry.line.startswith(
                            ":",
                        ):
                            dev_path = ("", "/dev/")[
                                utmp_entry.line[0] != "/"
                            ] + utmp_entry.line
                            idle = _datetime.fromtimestamp(
                                _stat(dev_path).st_atime,
                            )
                            if idle.tzinfo is None:
                                idle = idle.replace(tzinfo=_timezone.utc)

                        sessions_by_user_login[utmp_entry.user].append(
                            _FingerSession(
                                start=start,
                                idle=idle,
                                line=utmp_entry.line,
                                host=utmp_entry.host,
                            ),
                        )

                users: list[_FingerUser] = []
                for pw_entry in _pwd.getpwall():
                    if (_Path(pw_entry.pw_dir) / ".nofinger").exists():
                        continue

                    office = None
                    gecos = pw_entry.pw_gecos.split(",")
                    if len(gecos) >= 2:
                        office = gecos[1]

                    plan = None
                    try:
                        with open(
                            _Path(pw_entry.pw_dir, ".plan"),
                        ) as plan_file:
                            plan = plan_file.read()
                    except (FileNotFoundError, PermissionError):
                        pass

                    # We may have a lastlog entry
                    sessions = sessions_by_user_login.get(pw_entry.pw_name, [])
                    last_login = lastlog_by_user_id.get(pw_entry.pw_uid)
                    if sessions:
                        session_times = [session.start for session in sessions]
                        if last_login is not None:
                            session_times.append(last_login)

                        last_login = max(session_times)

                    users.append(
                        _FingerUser(
                            login=pw_entry.pw_name,
                            name=gecos[0],
                            shell=pw_entry.pw_shell,  # noqa: S604
                            home=pw_entry.pw_dir,
                            office=office,
                            plan=plan,
                            last_login=last_login,
                            sessions=sessions,
                        ),
                    )

                # We're done refreshing!
                self._data = users
                self._lastrefreshtime = _datetime.utcnow()

            return tuple(
                user
                for user in self._data
                if (
                    (query is None or query in user.login)
                    and (active is None or active == bool(user.sessions))
                )
            )
        finally:
            self._lock.release()
