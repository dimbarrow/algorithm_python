lst = [1,2,3,4,5,6,2,3,4,2,1]

def counting_sort(lst):
    t_lst = [0]*len(lst)
    s_lst = []
    for i in range(len(lst)):
        t_lst[lst[i]] += 1

    for i in range(len(t_lst)):
        s_lst += [i] * t_lst[i]

    return s_lst


print(counting_sort(lst))