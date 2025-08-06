
from itertools import combinations


N = int(input())
list_elements = input().split()
K = int(input())
list_comb = list(combinations(list_elements,K))

count = 0
for comb in list_comb:
    if "a" in comb:
        count+=1

probability = count/len(list_comb)

print("{0:.4f}".format(probability))