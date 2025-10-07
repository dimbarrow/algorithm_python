def addBinary(a, b):
    ost = list()
    c = int(a, 2) + int(b, 2)
    if c == 0:
        return "0"
    while c > 0:
        ost.append(c%2)
        c = c//2
        print(c)

    new_ost = ''
    for i in range(len(ost), 0 ,-1):
        new_ost += str(ost[i-1])
    return new_ost