from itertools import combinations

K,M = list(map(int,input().split()))
arr = []
for _ in range(K):
    line = list(map(int,input().split()))
    arr.append(line[1:])

possible_sum = {0}

for block in arr:
    new_sum = set()
    for value in block:
        for s in possible_sum:
            new_sum.add((s + pow(value,2))%M)
    possible_sum = new_sum
print(max(possible_sum))


