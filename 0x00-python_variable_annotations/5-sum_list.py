#!/usr/bin/env python3
"""
Module of a type-annotated function sum_list
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result as a float.
    """
    return sum(input_list)
