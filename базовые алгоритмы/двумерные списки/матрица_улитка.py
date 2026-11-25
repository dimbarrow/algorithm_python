def matrix_snail(matrix):
    res = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if len(matrix[0]) - r - 1 == c: #
                if len(matrix[0])-1 == r:
                    print(matrix[r][c])
                    res.append(matrix[r][len(matrix)-c-1])
                elif len(matrix)-r-1 == c:
                    res.append(matrix[r][c])
            if len(matrix[0])-1 == c:
                res.append(matrix[r][c])
            
    return res


print(matrix_snail([[1,2,3],[4,5,6],[7,8,9]]))

