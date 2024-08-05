#!/usr/bin/env python3
from typing import Union, Tuple
"""
Model of a type-annotated function to_kv
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, and returns a tuple
    """
    return (k, float(v ** 2))
