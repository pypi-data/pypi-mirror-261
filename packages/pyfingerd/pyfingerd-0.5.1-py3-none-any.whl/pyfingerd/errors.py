#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""This file defines the exceptions used throughout the module."""

from __future__ import annotations


__all__ = [
    "BindError",
    "ConfigurationError",
    "HostnameError",
    "InvalidBindError",
    "MalformedRequestError",
    "NoBindsError",
]

# ---
# Configuration-related errors.
# ---


class ConfigurationError(Exception):
    """Raised when an invalid configuration option is set."""

    __slots__ = ()


class HostnameError(ConfigurationError):
    """Raised when a host name is invalid.

    :param hostname: The invalid hostname.
    """

    __slots__ = ()

    def __init__(self, /, *, hostname: str):
        super().__init__(f"Invalid host name {hostname!r}.")


class BindError(ConfigurationError):
    """Raised when an error has occurred with the provided binds.

    :param msg: The precise error message.
    """

    __slots__ = ("original_message",)

    def __init__(self, msg: str, /):
        self.original_message = msg
        super().__init__(
            f"An error has occurred with the provided binds: {msg}",
        )


class NoBindsError(BindError):
    """Raised when no binds were provided."""

    __slots__ = ()

    def __init__(self, /):
        super().__init__("No valid bind")


class InvalidBindError(BindError):
    """Raised when one of the provided binds came out erroneous.

    :param msg: The precise error message.
    :param bind: The bind that has failed.
    """

    __slots__ = ("original_message",)

    def __init__(self, msg: str = "", /, *, bind: str):
        super().__init__(
            f"One of the provided bind ({bind!r}) "
            + f'was invalid{": " + msg if msg else ""}',
        )

        if msg is not None:
            self.original_message = msg


class MalformedRequestError(Exception):
    """Raised when a malformed query is received.

    :param msg: The precise message.
    :param line: The malformed query line.
    """

    __slots__ = ("line", "msg")

    def __init__(
        self,
        msg: str,
        /,
        *,
        line: str,
    ) -> None:
        self.line = line
        self.msg = msg

        super().__init__(
            msg + (f": {line!r}" if line else "") + ".",
        )
