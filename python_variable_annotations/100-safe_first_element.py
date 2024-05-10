#!/usr/bin/env python3


"""
import List, Union and TypeVar from typing
correct duck-typed annotations
"""
from typing import List, Union, TypeVar, Sequence


T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Union[T, None]:
    """
    function safe_first_element
    parameters
        lst: list
    """
    if lst:
        return lst[0]
    else:
        return None
