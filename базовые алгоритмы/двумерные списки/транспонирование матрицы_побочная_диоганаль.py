import random
def kr_vivod(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def generate_matrix(n):
    matrix = [[random.randint(1,100) for j in range(n)] for i in range(n)]
    for i in range(n):
        print(matrix[i])
    print(' ')
    print('############')
    print(' ')

    c = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)-row-1):
            matrix[row][column], matrix[len(matrix)-1-column][len(matrix)-1-row] = matrix[len(matrix)-1-column][len(matrix)-1-row], matrix[row][column]
        c += 1

    return kr_vivod(matrix)


print(generate_matrix(3))