# bs approach using DFS that will go upto n^2 sing grid search and to be specific TC- 0(log n^2 . n^2) and space n^2
from collections import deque
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

m=len(arr[0])
l=arr[0][0]
h=max(max(i) for i in arr)
def valid(i,j,n,m):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    return True
def bfs(arr,i,j,money):
    q=deque()
    x=[-1,1,0,0]
    y=[0,0,-1,1]
    vis=[[0]*m for i in range(n)]
    q.append((0,0))
    vis[0][0]=1
    while q:
        r,c=q.popleft()
        if (r==n-1 and c==m-1):
            return True
        for k in range(4):
            ro=r+x[k]
            co=c+y[k]
            if valid(ro,co,n,m) and vis[ro][co]==0 and money>=arr[ro][co]:
                q.append((ro,co))
                vis[ro][co]=1
    return False
while l<=h:
    mid=(l+h)//2
    if bfs(arr,n,m,mid):
        res=mid
        h=mid-1
    else:
        l=mid+1
print(res)