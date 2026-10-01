def resh(n):
    lst = [0]*n
    for i in range(n):
        lst[i] = True

    lst[0] = False
    lst[1] = False
    for i in range(2, n):
        if lst[i]:
            for j in range(2*i, n, i):
                lst[j] = False

    return lst


print(resh(15))