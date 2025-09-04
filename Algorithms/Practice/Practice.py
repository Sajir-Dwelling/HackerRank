from collections import Counter
import math

def sales_by_match(n,ar):
    counting = Counter(ar)
    pair = 0

    if not ar:
        return 0

    for value in counting.values():
        pair += value//2
    return pair

if __name__=="__main__":
    n = int(input())
    ar = list(map(int,input().split()))
    print(sales_by_match(n,ar))