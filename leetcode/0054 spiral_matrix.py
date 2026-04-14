def spiralOrder(matrix):
    up = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    spiral = []

    while up <= down and left <= right:
        for i in range(left, right + 1):
            spiral.append(matrix[up][i])
        up += 1

        for j in range(up, down + 1):
            spiral.append(matrix[j][right])
        right -= 1

        if up <= down:
            for k in range(right, left - 1, -1):
                spiral.append(matrix[down][k])
            down -= 1

        if left <= right:
            for l in range(down, up - 1, -1):
                spiral.append(matrix[l][left])
            left += 1

    return spiral

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))