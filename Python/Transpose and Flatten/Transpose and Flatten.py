

import numpy as np

N,M = list(map(int,input().split()))
list_arr = []
for _ in range(N):
    a = list(map(int,input().split()))
    list_arr.append(a)

arr = np.array(list_arr)
print(np.transpose(arr))
print(arr.flatten())