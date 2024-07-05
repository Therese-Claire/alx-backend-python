#!/usr/bin/env python3
"""Task 9 module"""
from typing import List


def element_length(lst: List[int]) -> int:
    return [(i, len(i)) for i in lst]
