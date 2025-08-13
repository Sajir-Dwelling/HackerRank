
if __name__ == "__main__":
    n = int(input())
    list_elem = []
    for i in range(n):
        command = input().split()
        if command[0] == "insert":
            list_elem.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(list_elem)
        elif command[0] == "remove":
            list_elem.remove(int(command[1]))
        elif command[0] == "append":
            list_elem.append(int(command[1]))
        elif command[0] == "sort":
            list_elem.sort()
        elif command[0] == "pop":
            list_elem.pop()
        elif command[0] == "reverse":
            list_elem.reverse()
