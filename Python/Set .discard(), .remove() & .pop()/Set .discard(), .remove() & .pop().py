
n = int(input())
s = set(map(int,input().split()))
N = int(input())

for _ in range(N):
    user_input = input().split()
    command = user_input[0]
    if command in ["remove", "discard"]:
        k = int(user_input[1])
        if command=="remove":
            try:
                s.remove(int(k))
            except KeyError:
                pass
        elif command=="discard":
            s.discard(int(k))
    elif command=="pop":
        try:
            s.pop()
        except KeyError:
            pass

print(sum(s))