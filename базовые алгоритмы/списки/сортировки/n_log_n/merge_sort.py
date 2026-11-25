def merge_sort(lst):
    if len(lst) < 2:
        return lst

    n = len(lst)//2
    left = merge_sort(lst[n:])
    right = merge_sort(lst[:n])
    return merge(left, right)

def merge(l, r):
    l_counter = 0
    r_counter = 0
    n = 0
    result = [0]*(len(l)+len(r))
    while l_counter < len(l) and r_counter < len(r):
        if l[l_counter] <= r[r_counter]:
            result[n] = l[l_counter]
            l_counter += 1
            n += 1
        else:
            result[n] = r[r_counter]
            r_counter += 1
            n += 1

    while l_counter < len(l):
        result[len(r)+l_counter] = l[l_counter]
        l_counter += 1

    while r_counter < len(r):
        result[len(l)+r_counter] = r[r_counter]
        r_counter += 1

    return result



print(merge_sort([5,2,4,3,1,7,8]))
