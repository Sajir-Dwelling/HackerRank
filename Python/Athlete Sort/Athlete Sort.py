import math
import os
import random
import re
import sys

user_input = input().split()
N = int(user_input[0])
M = int(user_input[1])

arr = []

for _ in range(N):
    name_of_attribute =list(map(int,input().split()))
    arr.append(name_of_attribute)
k = int(input())

arr.sort(key=lambda x:x[k])

for row in arr:
    print(" ".join(map(str,row)))