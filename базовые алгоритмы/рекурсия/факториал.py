def factorial(n, f):
    if n == 1:
        print(f)
    else:
        f *= n
        factorial(n-1, f)

factorial(5, 1)