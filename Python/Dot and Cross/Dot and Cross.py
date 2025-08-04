import numpy as np

N = int(input())

A = []
B = []

for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)


multiplication = np.dot(A,B)
print(multiplication)