#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here

    count_a = s.count("a")

    complete_repeat = n//len(s)

    remaining_char = n%len(s)

    count_in_remaining = s[:remaining_char].count("a")

    total_count = (count_a*complete_repeat)+count_in_remaining

    return total_count
if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
