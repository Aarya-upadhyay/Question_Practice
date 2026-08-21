from collections import  deque
n=int(input())
e=int(input())
edges=[]
for i in range(e):
    edges.append(list(map(int,input().split())))

adj=[[] for i in range(n)]
for i in range(e):
    s=edges[i][0]
    d=edges[i][1]
    adj[s].append(d)
    adj[d].append(s)


q=deque()
vis=[0]*n
res=[]
dis=0
src=int(input())
des=int(input())
def bfs(adj,vis,src,des,dis):
    q.append((src,0))
    vis[src]=1
    
    while q:
        sr,di=q.popleft()
        res.append(di)
        for i in range(len(adj[sr])):
            nei=adj[sr][i]
            if vis[nei]==0:
                q.append((nei,di+1))
                vis[nei]=1
    print(res)
    return res[des] if res[des]!=0 else -1
print(bfs(adj,vis,src,des,dis))
    
