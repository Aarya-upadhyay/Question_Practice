n = int(input("enter no of rows: "))
m = int(input("enter no of cols: "))

grid = []

for i in range(n):
    grid.append(list(map(int,input().split())))

def noof(grid):
    n=len(grid)
    visi=[False]*n
    res=0
    def dfs(city):
        visi[city]=True
        for i in range(n):
            if grid[city][i]==1 and not visi[i]:
                dfs(i)
    for i in range(n):
        if not visi[i]:
            dfs(i)
            res+=1
    return res
print(noof(grid))
