<<<<<<< HEAD
def swap_case(s):
    new_s = []
    for item in s:
        if item.isalpha():
            if item.isupper():
                new_s.append(item.lower())
            else:
                new_s.append(item.upper())
        else:
            new_s.append(item)

    return ''.join(new_s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
=======
def swap_case(s):
    new_s = []
    for item in s:
        if item.isalpha():
            if item.isupper():
                new_s.append(item.lower())
            else:
                new_s.append(item.upper())
        else:
            new_s.append(item)

    return ''.join(new_s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
>>>>>>> 213b2ac (Added new files and folders)
    print(result)