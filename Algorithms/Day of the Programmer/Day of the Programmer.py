#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    list_leap = [31, 29, 31, 30, 31, 30, 31, 31]
    list_non_leap = [31, 28, 31, 30, 31, 30, 31, 31]

    if year == 1918:
        return "26.09.1918"

    if year < 1918:
        is_leap = (year % 4 == 0)

    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if is_leap:
        date = 256 - sum(list_leap)
    else:
        date = 256 - sum(list_non_leap)

    return f"{date}.09.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
