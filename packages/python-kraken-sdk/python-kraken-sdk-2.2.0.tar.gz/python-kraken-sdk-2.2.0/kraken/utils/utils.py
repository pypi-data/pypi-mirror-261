#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 Benjamin Thomas Schwertfeger
# GitHub: https://github.com/btschwertfeger

"""Module implementing utility functions used across the package"""

from __future__ import annotations

import warnings
from functools import wraps
from typing import Any, Callable


def deprecated(func: Callable) -> Callable:
    """
    Function used as decorator to mark decorated functions as deprecated.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        warnings.warn(
            f"Call to deprecated function {func.__name__}.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        return func(*args, **kwargs)

    return wrapper


__all__ = ["deprecated"]
