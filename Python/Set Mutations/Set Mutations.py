

n = int(input())
A = set(map(int,input().split()))
N = int(input())

for _ in range(N):
    user_input = input().split()
    operation = user_input[0]
    length = user_input[1]
    s = set(map(int, input().split()))
    if operation == "intersection_update":
        A.intersection_update(s)
    elif operation == "update":
        A.update(s)
    elif operation == "symmetric_difference_update":
       A.symmetric_difference_update(s)
    elif operation == "difference_update":
        A.difference_update(s)

print(sum(A))