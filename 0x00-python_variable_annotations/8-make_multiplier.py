#!/usr/bin/env python3
"""Task 8 module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.

    Args:
        multiplier: float multiplier

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the multiplier.
    """
    return lambda x: x * multiplier
