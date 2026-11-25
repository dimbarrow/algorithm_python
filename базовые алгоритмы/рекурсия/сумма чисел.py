def sum_nums(n, f):
    if n == 1:
        print(f+1)
    else:
        f += n
        sum_nums(n-1, f)

sum_nums(3, 0)