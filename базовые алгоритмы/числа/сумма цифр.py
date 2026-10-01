def sum_num_universal(n):
    summ = 0
    num = 10
    for i in range(len(str(n))):
        print(n%num)
        summ += n%num
        num *= 10
        n//=10

    return summ

def sum_num_py(n):
    n = str(n)
    summ = 0
    for i in range(len(str(n))):
        summ += int(n[i])

    return summ


print(sum_num_universal(12))
print(sum_num_py(12))