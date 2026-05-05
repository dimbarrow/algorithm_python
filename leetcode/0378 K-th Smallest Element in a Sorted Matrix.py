def k_th_smallest(matrix, k):
    lst = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lst.append(matrix[i][j])
    lst.sort()

    return lst[k-1]