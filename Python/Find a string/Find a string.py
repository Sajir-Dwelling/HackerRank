def count_substring(string, sub_string):
    start = 0
    end = len(sub_string)

    count = 0

    while end <= len(string):
        if sub_string == string[start:end]:
            count += 1
        start += 1
        end += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)