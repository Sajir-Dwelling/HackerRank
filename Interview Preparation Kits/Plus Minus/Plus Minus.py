#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pcount,ncount,zcount = 0,0,0

    for i in arr:
        if i>0:
            pcount+=1
        if i==0:
            zcount+=1
        if i<0:
            ncount+=1

    Positive_ratio =  pcount/n
    Negative_ratio =  ncount/n
    Zero_ratio = zcount/n

    print('{:.6f}'.format(Positive_ratio))
    print('{:.6f}'.format(Negative_ratio))
    print('{:.6f}'.format(Zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
