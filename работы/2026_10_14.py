def island_perimeter(grid):
    rows = len(grid)
    columns = len(grid[0])
    per = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                per +=4
                if row > 0 and grid[row-1][column] == 1:
                    per -= 2
                if column > 0 and grid[row][column-1] == 1:
                    per -= 2

    return per



print(island_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(island_perimeter([[1]]))