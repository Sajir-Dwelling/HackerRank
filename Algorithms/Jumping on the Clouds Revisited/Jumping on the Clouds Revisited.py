#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy_level = 100
    current = 0
    for i in range(len(c)):
        current = (current+k)%n
        energy_level-=1

        if c[current] == 1:
            energy_level-=2

        if current==0:
            break
    return energy_level

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
