#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_rows = []
    for row in grid:
        sorted_row = sorted(row)
        sorted_rows.append(sorted_row)
    for col in range(len(sorted_rows[0])):
        for row in range(1,len(sorted_rows)):
            if sorted_rows[row][col] < sorted_rows[row-1][col]:
                return "NO"
    return "YES"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)