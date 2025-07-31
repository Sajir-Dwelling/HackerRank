def avg(arr):
    arr_set = set(arr)
    result = sum(arr_set)/len(arr_set)
    return result

if __name__=="__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    average = avg(arr)
    print(average)