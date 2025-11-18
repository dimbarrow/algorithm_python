import random
import time
test1 = []
test2 = []
for i in range(1500):
    test1.append(random.randint(1, 150))
test2 = [0] * len(test1)
for i in range(len(test1)):
    test2[i] = test1[i]

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        num = lst[0]
        less = [i for i in lst[1:] if i < num]

        more = [i for i in lst[1:] if i >= num]

        return quicksort(less) + [num] + quicksort(more)


def merge_sort(lst):
    if len(lst) < 2:
        return lst


    mid_lst = len(lst) // 2
    left_lst = merge_sort(lst[mid_lst:])
    right_lst = merge_sort(lst[:mid_lst])

    return merge(left_lst, right_lst)

def merge(l, r):
    k = 0
    j = 0
    n = 0
    result = [0] * (len(l)+len(r))
    while k < len(l) and j < len(r):
        if l[k] <= r[j]:
            result[n] = l[k]
            k += 1
            n += 1
        else:
            result[n] = r[j]
            j += 1
            n += 1

    while k < len(l):
        result[len(r) + k] = l[k]
        k += 1
    while j < len(r):
        result[len(l) + j] = r[j]
        j += 1

    return result

time_start1 = time.time()
print(quicksort(test1))
time_end1 = time.time()
time_start2 = time.time()
print(merge_sort(test2))
time_end2 = time.time()

print(time_end1-time_start1)
print(time_end2-time_start2)