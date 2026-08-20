n=int(input())
e=int(input())
edges=[]
for _ in range(e):
    edges.append(list(map(int,input().split())))
ind=[0]*n
adj=[[] for i in range(n)]
for i in range(e):
    src=edges[i][0]
    des=edges[i][1]
    adj[src].append(des)
    ind[des]+=1
from collections import deque
q=deque()
def bfs(adj,ind):
    for i in range(n):
        if ind[i]==0:
            q.append(i)
    res=[]
    while q:
        node=q.popleft()
        res.append(node)
        for i in range(len(adj[node])):
            nei=adj[node][i]
            ind[nei]-=1
            if ind[nei]==0:
                q.append(nei)
    return res
print(bfs(adj,ind))

def dfs(adj):
    stack=[]
    visi=[0]*n
    def path(node):
        visi[node]=1
        for n in adj[node]:
            if visi[n]==0:
                path(n)
        stack.append(node)
    for i in range(n):
        if visi[i]==0:
            path(i)
    stack.reverse()
    return stack
print(dfs(adj))


    
    

