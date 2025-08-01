
n = int(input())
english_roll = set(map(int,input().split()))
b = int(input())
french_roll = set(map(int,input().split()))

total_num = len(english_roll.intersection(french_roll))
print(total_num)