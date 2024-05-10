#!/usr/bin/env python3


"""
import List and Tuple from typing
define function element_lenght
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    function ellement_length
    paramesters
        lst: list
    returns a list
    """

    return [(i, len(i)) for i in lst]
