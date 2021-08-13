#!/usr/bin/python3
"""Minimun operations"""


def minOperations(n):
    """Calculate the fewest number of operations needed to copyall/paste operations.

    Args:
        n: Number of operations to find

    Returns:
        int: number of operations to execute.
    """
    number = 1
    copy = 0
    operations = 0
    if type(n) is not int or n < 2:
        return 0
    else:
        for i in range(n):
            if number == n:
                return operations
            elif n % number == 0:
                copy = number
                number += copy
                operations += 2
            else:
                number += copy
                operations += 1
