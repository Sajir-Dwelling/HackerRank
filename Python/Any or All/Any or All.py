



N = int(input())
arr = list(map(int,input().split()))

condition1 = all(i>0 for i in arr)
condition2 = any(str(i) == str(i)[::-1] for i in arr)

print(condition1 and condition2)