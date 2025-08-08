cube = lambda x: pow(x,3)# complete the lambda function


# Online Python - IDE, Editor, Compiler, Interpreter
def fibonacci(n):
    fib_series = [0, 1]

    if n == 0:
        return []
    elif n == 1:
        return [0]

    for i in range(2, n):
        next_sum = fib_series[-1] + fib_series[-2]
        fib_series.append(next_sum)
    return fib_series


if __name__ == "__main__":
    n = int(input())
    fibonacci(n)
    print(list(map(cube, fibonacci(n))))