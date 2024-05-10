#!/usr/bin/env python3


"""
define a function sum_mixed_list
"""


def sum_mixed_list(mxd_lst: list[float]) -> float:
    """
    function sum_mixed_list
    parameters:
        mxd_lst: list of integers and floats
    returns arguments sum as a float
    """

    total = 0.0
    for num in mxd_lst:
        total += num
    return total
