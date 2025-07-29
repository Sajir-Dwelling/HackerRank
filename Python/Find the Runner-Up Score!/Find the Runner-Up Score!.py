if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for score in range(len(arr)):
        if arr[score] != arr[score+1]:
            print(arr[score+1])
            break
        else:
            continue

