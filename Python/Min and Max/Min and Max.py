import numpy as np

N,M = list(map(int,input().split()))

A = []

for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)

B = np.min(A ,axis = 1)
print(np.max(B))