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

def tabulation(grid,m,n):
    dp=[[0]*n for _ in range(m)]
    dp[m-1][n-1]=1
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                continue
            if grid[i][j]==1:
                dp[i][j]=0
                continue
            d=0
            r=0
            if i+1<m:
                d=dp[i+1][j]
            if j+1<n:
                r=dp[i][j+1]
            dp[i][j]=d+r
    return dp[0][0]
n=len(grid[0])
print(tabulation(grid,m,n))


def uniquePathsWithObstacles(grid):

    m = len(grid)
    n = len(grid[0])

    dp = [0] * n
    dp[n-1] = 1

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):

            if grid[i][j] == 1:
                dp[j] = 0
            elif j + 1 < n:
                dp[j] = dp[j] + dp[j+1]

    return dp[0]
print(uniquePathsWithObstacles(grid))
