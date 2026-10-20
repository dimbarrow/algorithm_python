def rotate_45(matrix):
    res = [[0]*(2*len(matrix)-1) for _ in range(2*len(matrix)-1)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            r = i + j
            c = len(matrix)+j-i-1
            res[r][c] = matrix[i][j]

    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    print(matrix[i])

print('##############')

for i in range(len(rotate_45(matrix))):
    print(rotate_45(matrix)[i])