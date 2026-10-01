def from_sys_to_sys(num, sys1, sys2):
    lst = list()
    num = int(str(num), sys1)
    while num >= sys2:
        lst.append(num % sys2)
        num //= sys2
    lst.append(num)

    return lst[::-1]

print(from_sys_to_sys(123, 3, 2))