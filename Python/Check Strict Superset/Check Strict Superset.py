# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int,input().split()))
n = int(input())
boolean = True

for i in range(n):
    other_set = set(map(int,input().split()))

    if not other_set.issubset(A):
        boolean = False
        if len(other_set)>= len(A):
            boolean = False

print(boolean)

