


M = int(input())
A = set(map(int,input().split()))
N = int(input())
B = set(map(int,input().split()))

sym_diff = list(sorted(A.symmetric_difference(B)))

for i in sym_diff:
    print(i)