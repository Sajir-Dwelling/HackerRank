import re

S = input()

match =  re.search(r"([a-zA-Z0-9])\1",S)

if match:
    print(match.group(1))
else:
    print(-1)