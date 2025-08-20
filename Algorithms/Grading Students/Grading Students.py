#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []

    for grade in grades:
        if grade < 38:
            result.append(grade)

        else:
            round_list = math.ceil(grade/5)
            next_multiple = round_list*5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    return result


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
