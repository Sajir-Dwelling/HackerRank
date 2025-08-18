#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here

    turns_front = p//2
    turns_back = (n//2) - (p//2)

    return min(turns_front,turns_back)




if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)