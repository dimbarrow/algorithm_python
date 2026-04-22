def generateMatrix(n):
    matrix = [[0]*n for i in range(n)]

    print(matrix)

    up = 0
    down = n-1
    left = 0
    right = n-1
    counter = 0
    while left <= right and up <= down:
        print('Запуск')
        for i in range(left, right+1):
            matrix[up][i] = counter
            print(counter)
            print(matrix[up][i])
            print(matrix)
            input()
            counter += 1
        up += 1

        for j in range(up, down+1):
            matrix[right][j] = counter
            print(counter)
            print(matrix[right][j])
            print(matrix)
            input()
            counter += 1
        right -= 1

        for i in range(right, left-1, -1):
            matrix[down][i] = counter
            print(counter)
            print(matrix[down][i])
            print(matrix)
            input()
            counter += 1
        down -= 1

        for j in range(down, up-1, -1):
            matrix[left][j] = counter
            print(counter)
            print(matrix[left][j])
            print(matrix)
            input()
            counter += 1
        left += 1

    return matrix


def generateMatrix_2(n):
    matrix = [[0] * n for i in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    num = 1

    while num <= n*n:
        #Заполняю верхнюю строку
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1 #верхняя граница опускается вниз

        #Заполняю правый столбец
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1 #правая граница сдвигается влево

        #Заполняю нижнюю строку
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1 #нижняя граница поднимается вверх

        #Заполняю левый столбец
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1 #левая граница сдвигается вправо

    return matrix

print(generateMatrix_2(3))