
n = int(input())
english_roll = set(map(int,input().split()))
b = int(input())
french_roll = set(map(int,input().split()))

total_num = english_roll.symmetric_difference(french_roll)
print(len(total_num))