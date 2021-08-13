#!/usr/bin/python3
"""Min operations"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to copyall/paste.
    """
    numFind = 1
    numTemp = 0
    operations = 0
    if type(n) is not int or n < 2:
        return 0
    else:
        for i in range(n):
            if numFind == n:
                return operations
            elif n % numFind == 0:
                numTemp = numFind
                numFind += numTemp
                operations += 2
            else:
                numFind += numTemp
                operations += 1
