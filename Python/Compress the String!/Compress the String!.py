from itertools import groupby

S = input().strip()
groups = groupby(S)
for key, group in groups:
    count = len(list(group))
    print(f"({count}, {key})", end= " ")
