def b_sort(st):
    for i in range(len(st)):
        for g in range(len(st)-1):
            if st[g] > st[g+1]:
                st[g], st[g+1] = st[g+1], st[g]

    return st


print(b_sort([1, 3, 5, 2 ,5]))