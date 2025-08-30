#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    result = []
    for i in range(1,n+1):
        result.append(i)

    factorial = 1
    for j in result:
        factorial*=j
    print(factorial)


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
