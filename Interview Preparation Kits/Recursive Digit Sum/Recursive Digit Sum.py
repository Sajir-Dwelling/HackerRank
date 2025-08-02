#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    digital_sum = sum(int(d) for d in n)

    total_sum = digital_sum*k

    def compute_sup_digit(num):
        if num<10:
            return num

        sum_digits = sum(int(d) for d in str(num))
        return compute_sup_digit(sum_digits)

    return compute_sup_digit(total_sum)



if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)
