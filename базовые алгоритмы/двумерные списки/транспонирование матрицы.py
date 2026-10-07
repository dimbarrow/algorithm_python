import random
def generate_matrix(n):
    matrix = [[0]*n]*n
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(1, 15)
    matrix[0][1] = 2
    return matrix

print(generate_matrix(3))