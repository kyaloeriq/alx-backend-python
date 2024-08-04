#!/usr/bin/env python3
"""
Model of a type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.
    """
    return sum(mxd_lst)
