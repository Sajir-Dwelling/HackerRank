import numpy as np

N,M = list(map(int,input().split()))

A = []

for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)
A = np.array(A)

print(np.mean(A,axis = 1))
print(np.var(A,axis = 0))
B = np.std(A,axis = None)
print(round(B,11))
