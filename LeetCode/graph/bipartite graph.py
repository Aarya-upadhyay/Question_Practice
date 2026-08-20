n=int(input())
e=int(input())
edges=[]
for i in range(e):
    edges.append(list(map(int,input().split())))
res=False
adj=[[] for i in range(n)]
for i in range(e):
    src=edges[i][0]
    des=edges[i][1]
    adj[src].append(des)
    adj[des].append(src)

def dfs(adj,node,c,color):
    color[node]=c
    for i in range(len(adj[node])):
        nei=adj[node][i]
        if color[nei]!=-1 and color[nei]==c:
            return False
        if color[nei]==-1:
            if not dfs(adj,nei,1-c,color):
                return False
    return True
color=[-1]*n
for i in range(n):
    if color[i]==-1:
        if dfs(adj,i,0,color):
            res=True
            break
print(res)