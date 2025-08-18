#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    num_highest_score = 0
    num_lowest_score = 0

    if not scores:
        return num_highest_score, num_lowest_score

    highest_score = [scores[0]]
    lowest_score = [scores[0]]

    for score in scores:
        if score > highest_score[-1]:
            highest_score.append(score)
        elif score < lowest_score[-1]:
            lowest_score.append(score)

    num_highest_score = len(highest_score[1:])
    num_lowest_score = len(lowest_score[1:])

    return num_highest_score, num_lowest_score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
