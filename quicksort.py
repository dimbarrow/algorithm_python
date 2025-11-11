def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        num = lst[0]
        less = [i for i in lst[1:] if i < num]

        more = [i for i in lst[1:] if i > num]

        return quicksort(less) + [num] + quicksort(more)

print(quicksort([2, 10, 4, 5]))
