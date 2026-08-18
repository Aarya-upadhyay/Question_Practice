n = int(input("enter no of rows: "))
m = int(input("enter no of cols: "))

grid = []

for i in range(n):
    grid.append(input().split())


def valid(i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return True


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]


def island(arr, n, m, i, j, visited):
    visited[i][j] = 1

    for k in range(4):
        row = i + x[k]
        col = j + y[k]

        if valid(row, col, n, m) and arr[row][col] == '1' and visited[row][col] == 0:
            island(arr, n, m, row, col, visited)

    return


def noofisland(grid):
    n = len(grid)
    m = len(grid[0])

    res = 0

    visited = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and visited[i][j] == 0:
                island(grid, n, m, i, j, visited)
                res += 1

    return res


print(noofisland(grid))