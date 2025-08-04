

import numpy as np
np.set_printoptions(legacy='1.13')
N = int(input())
A = []

for _ in range(N):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)

print(np.linalg.det(A))