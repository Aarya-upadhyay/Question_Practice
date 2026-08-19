n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

def valid(i,j,n,m):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    return True

x=[-1,1,0,0]
y=[0,0,-1,1]

from collections import deque

def bfs(arr):
    n=len(arr)
    m=len(arr[0])
    q=deque()
    fresh=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:
                q.append((i,j))
            elif arr[i][j]==1:
                fresh+=1
    t=0
    while q and fresh>0:
        size=len(q)
        for _ in range(size):
            i,j=q.popleft()
            for k in range(4):
                row=i+x[k]
                col=j+y[k]
                if valid(row,col,n,m) and arr[row][col]==1:
                    arr[row][col]=2
                    fresh-=1
                    q.append((row,col))
        t+=1
    if fresh>0:
        return -1
    return t
print(bfs(arr))