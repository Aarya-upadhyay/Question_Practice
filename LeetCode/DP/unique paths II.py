m=int(input())
grid=[]
for _ in range(m):
    grid.append(list(map(int,input().split())))

n=len(grid[0])
"""def uni(grid,i,j):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n or grid[i][j]==1:
        return 0
    down=uni(grid,i+1,j)
    right=uni(grid,i,j+1)
    ans=down+right
    return ans
print(uni(grid,0,0))
"""
t=[[-1]*n for _ in range(m)]
def dp(grid,i,j,t):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n or grid[i][j]==1:
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    down=dp(grid,i+1,j,t)
    right=dp(grid,i,j+1,t)
    ans=down+right
    t[i][j]=ans
    return ans
print(dp(grid,0,0,t))