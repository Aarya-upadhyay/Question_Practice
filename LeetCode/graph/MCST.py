import heapq
n=int(input())
edges=[]
e=int(input())
for _ in range(e):
    edges.append(list(map(int,input().split())))

adj=[[] for _ in range(n)]
for u,v,w in edges:
    adj[u].append((v,w))
    adj[v].append((u,w))
vis=[0]*n
heap=[]
def mst(adj,vis,res):
    heapq.heappush(heap,(0,0))
    while heap:
        s,d=heapq.heappop(heap)
        if vis[s]==1:
            continue
        vis[s]=1
        res+=d
        for i in range(len(adj[s])):
            nei=adj[s][i][0]
            wei=adj[s][i][1]
            if vis[nei]==0:
                heapq.heappush(heap,(nei,wei))
    return res
print(mst(adj,vis,0))
