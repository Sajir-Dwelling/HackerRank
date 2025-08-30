#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here

    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))

    return max(0,end-start+1)

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):

        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)
