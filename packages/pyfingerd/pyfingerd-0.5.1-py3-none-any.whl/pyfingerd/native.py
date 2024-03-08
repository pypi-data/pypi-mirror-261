#!/usr/bin/env python3
# *****************************************************************************
# Copyright (C) 2017-2022 Thomas Touhey <thomas@touhey.fr>
# This file is part of the pyfingerd project, which is MIT-licensed.
# *****************************************************************************
"""Defining the native interface."""

from __future__ import annotations

from .core import FingerInterface as _FingerInterface


__all__ = ["FingerNativeInterface", "FingerNoNativeFoundInterface"]

FingerNativeInterface: type[_FingerInterface]


class FingerNoNativeFoundInterface(_FingerInterface):
    """Placeholder interface that doesn't initiate.

    :py:attr:`FingerNativeInterface` is set to this class if no interface
    is available for the current platform.
    """

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "Could not find a suitable native interface.",
        )


try:
    from .posix import FingerPOSIXInterface as FingerNativeInterface  # NOQA
except ImportError:
    FingerNativeInterface = FingerNoNativeFoundInterface
