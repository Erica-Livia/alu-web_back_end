#!/usr/bin/env python3


from typing import List
"""
imported List from typing
define a function sum_mixed_list
"""


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """
    function sum_mixed_list
    parameters:
        mxd_lst: list of integers and floats
    returns arguments sum as a float
    """

    return sum(mxd_lst)
