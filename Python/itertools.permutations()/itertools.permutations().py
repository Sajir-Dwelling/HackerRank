# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    division,k = input().split()
    for item in sorted(list(permutations(division, int(k)))):
        print("".join(item))
