

def find_index(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
if __name__ == "__main__":
    lst = list(map(int,input().split()))
    target = int(input())
    result = find_index(lst,target)
    print(result)