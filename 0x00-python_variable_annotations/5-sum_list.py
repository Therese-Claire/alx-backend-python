#!/usr/bin/env python3
"""Task 5 module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function sum_list which takes a list
    input_list of floats as argument and returns their sum
    as a float.


    Args:
        input_list (float): list of floats

    Returns:
        float: sum of list items.
    """
    return float(sum(input_list))
