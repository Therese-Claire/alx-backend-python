#!/usr/bin/env python3
"""Task 6 module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float

    Args:
        mxd_lst (float & int): mixed list of float and int

    Returns:
        float: sum of mixed list.
    """
    return float(sum(mxd_lst))
