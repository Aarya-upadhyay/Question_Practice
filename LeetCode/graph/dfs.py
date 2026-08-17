n=int(input())
edges=[]
m=int(input())
for i in range(m):
    edges.append(list(map(int,input().split())))

adj=[[] for i in range(n)]
for i in edges:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])
"""
def dfs(adj,res,node,visited):
    res.append(node)
    print(node)
    visited[node]=True
    for i in range(len(adj[node])):
        nei=adj[node][i]
        if visited[nei]==False:
            dfs(adj,res,nei,visited)
    return res
def printd(adj):
    visited=[False]*n
    a=dfs(adj,[],0,visited)
    return a
print(printd(adj))
"""

def dfs(adj,no,res,visited):
    stack=[no]
    while stack:
        m=stack.pop()
        visited[m]=True
        res.append(m)
        for nei in adj[m]:
            if not visited[nei]:
                stack.append(nei)
    return res
visited=[False]*n
print(dfs(adj,0,[],visited))

