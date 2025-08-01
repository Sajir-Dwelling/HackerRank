
a = int(input())
b = int(input())

for i in list(divmod(a,b)):
    print(i)
print(divmod(a,b))