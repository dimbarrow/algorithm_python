def countAndSay(n):
    new_n = ''
    f = 0
    if n == 1:
        return n

    for i in range(len(n)):
        if n[f] != n[i]:
            new_n += str(i - f)
            new_n += n[f]
            f = i

    new_n += str(len(n) - f)
    new_n += n[f]

    return new_n


print(countAndSay("3322251"))