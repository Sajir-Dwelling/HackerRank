import numpy as np

n,m = list(map(int,input().split()))

A = []

for _ in range(n):
    row = list(map(int,input().split()))
    A.append(row)

#B = np.sum(A,axis=0)
#print(np.prod(B))

A = np.sum(A,axis=0)

product= 1
for num in A:
    product *= num
print(product)