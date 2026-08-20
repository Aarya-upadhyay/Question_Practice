n=int(input())
e=int(input())
edges=[]
for i in range(e):
    edges.append(list(map(int,input().split())))


adj=[[] for i in range(n)]
for i in range(e):
    src=edges[i][0]
    des=edges[i][1]
    adj[src].append(des)
    
path=[0]*n
visi=[0]*n
cycle=0
def dfs(adj,node,path,visi):
    visi[node]=1
    path[node]=1
    for i in range(len(adj[node])):
        ne=adj[node][i]
        if visi[ne]==1 and path[ne]==1:
            return True
        if visi[ne]==0:
            if dfs(adj,ne,path,visi):
                return True
    path[node]=0
    return False
 
for i in range(n):
    if visi[i]==0:
        if dfs(adj,i,path,visi):
            cycle=1
            break
print(cycle)

