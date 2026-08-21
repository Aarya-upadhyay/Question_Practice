n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(str,input().split())))

def valid(i,j,n,m):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    return True
x=[-1,1,0,0]
y=[0,0,-1,1]
def dfs(grid,i,j,n,m):
    grid[i][j]='#'
    for k in range(4):
        row=i+x[k]
        col=j+y[k]
        if valid(row,col,n,m) and grid[row][col]=='o':
            dfs(grid,row,col,n,m)
    return
m=len(grid[0])
def find(grid):
    n=len(grid)
    m=len(grid[0])
    for j in range(m):
        if grid[0][j]=='o':
            dfs(grid,0,j,n,m)
    for j in range(m):
        if grid[n-1][j]=='o':
            dfs(grid,n-1,j,n,m)
    for i in range(n):
        if grid[i][0]=='o':
            dfs(grid,i,0,n,m)
    for i in range(n):
        if grid[i][m-1]=='o':
            dfs(grid,i,m-1,n,m)
find(grid)
for i in range(n):
    for j in range(m):
        if grid[i][j]=='o':
            grid[i][j]='x'
        elif grid[i][j]=='#':
            grid[i][j]='o'
for i in range(n):
    for j in range(m):
        print(grid[i][j],end=' ')
    print()

