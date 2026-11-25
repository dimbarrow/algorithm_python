def quick_sort(lst):
    if len(lst) < 2:
        return lst

    center = lst[0]
    less = list()
    for i in range(1, len(lst)):
        if lst[i] < center:
            less.append(lst[i])

    more = list()
    for j in range(1, len(lst)):
        if lst[j] >= center:
            more.append(lst[j])

    less = quick_sort(less)
    more = quick_sort(more)
    res = list()
    for i in range(len(less)):
        res.append(less[i])
    print(center)
    res.append(center)
    for i in range(len(more)):
        res.append(more[i])
    return res


print(quick_sort([1,5,2,8,3,0]))