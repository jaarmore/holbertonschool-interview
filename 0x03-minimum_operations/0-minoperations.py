#!/usr/bin/python3
"""
Minimun operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to copyall/paste operations.
    """
    if n <= 1:
        return 0

    divisor = 2
    oper = 0
    quotient = n
    while quotient > 1:
        if (quotient % divisor) == 0:
            quotient = quotient // divisor
            oper += divisor
        else:
            divisor += 1

    return oper
