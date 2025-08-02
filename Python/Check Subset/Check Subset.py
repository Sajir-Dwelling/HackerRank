
T = int(input())

for _ in range(T):
    n = int(input())
    A = set(map(int,input().split()))
    m = int(input())
    B = set(map(int,input().split()))

    is_subset = True
    for i in A:
        if i not in B:
            is_subset = False
            break
    print(is_subset)

    #if A.issubset(B):
        #print("True")
    #else:
        #print("False")
