m=int(input())
n=int(input())
""" approach is wrong dude get it
grid=[[]*n for _ in range(m)]
def valid(i,j,m,n):
    if i<0 or i>=m or j<0 or j>=n:
        return False
    return True
visi=[[0]*n for _ in range(m)]
x=[1,0]
y=[0,1]
def dfs(grid,i,j,m,n):
    #visi[i][j]=1
    for k in range(2):
        ro=i+x[k]
        co=j+y[k]
        if valid(ro,co,m,n) :
            dfs(grid,ro,co,m,n)
res=0
for i in range(m):
    for j in range(n):
        
        dfs(grid,i,j,m,n)
        res+=1
print(res)4"""

"""
# recursion
def dfs(i,j):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n:
        return 0
    dow=dfs(i+1,j)
    rig=dfs(i,j+1)
    return dow+rig
print(dfs(0,0))
"""
#DP is folllowing since we would require the following case as well
grid=[[-1]*n for _ in range(m)]
def dfs(i,j,grid):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n:
        return 0
    if grid[i][j]!=-1:
        return grid[i][j]
    down=dfs(i+1,j,grid)
    right=dfs(i,j+1,grid)
    ans=down+right
    grid[i][j]=ans
    return ans
print(dfs(0,0,grid))