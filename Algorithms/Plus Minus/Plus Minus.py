


def plus_minus(n,arr):

    positive_list = []
    negative_list = []
    zero_list = []

    for num in arr:
        if num>0:
            positive_list.append(num)
        elif num<0:
            negative_list.append(num)
        elif num==0:
            zero_list.append(num)
    positive_ratio = len(positive_list)/len(arr)
    negative_ratio = len(negative_list)/len(arr)
    zero_ratio = len(zero_list)/len(arr)

    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__=="__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    plus_minus(n,arr)