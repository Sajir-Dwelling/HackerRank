
S = input()

lower = []
upper = []
odd = []
even = []

for char in S:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)
    elif char.isdigit():
        if int(char)%2==1:
            odd.append(char)
        else:
            even.append(char)
lower_sorted = sorted(lower)
upper_sorted = sorted(upper)
odd_sorted = sorted(odd)
even_sorted = sorted(even)

print("".join(lower_sorted+upper_sorted+odd_sorted+even_sorted))