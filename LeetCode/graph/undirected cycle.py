n=int(input())
e=int(input())
edges=[]
for _ in range(e):
    edges.append(list(map(int,input().split())))
adj=[[] for i in range(n)]
for i in range(e):
    src=edges[i][0]
    des=edges[i][1]
    adj[src].append(des)
    adj[des].append(src)
cycle=False
visi=[False]*n
def dfs(adj,n,node,par,visi):
    
    visi[node]=True
    
    for j in range(len(adj[node])):
        nei=adj[node][j]
        if visi[nei] and nei!=par:
            return True
        if not visi[nei]:
            dfs(adj,n,nei,node,visi)
            return True
    return False

for i in range(n):
    if not visi[i]:
        dfs(adj,n,i,-1,visi)
        cycle=True
print(cycle)
