#!/bin/python3

import math
import os
import random
import re
import string
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    # Write your code here
    result = []

    for c in s:
            if c.islower():
                result.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
            elif c.isupper():
                result.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
            else:
                result.append(c)

    return "".join(map(str,result))


if __name__ == '__main__':


    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)