# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
n = list(map(int,input().split()))

room_counts = Counter(n)

for room_num , room_count in room_counts.items():
    if room_count == 1:
        print(room_num)
