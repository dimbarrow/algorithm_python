def fib_num(n):
    x = 1
    y = 1
    for i in range(1, n):
        x, y = y, x+y

    return x


print(fib_num(4))