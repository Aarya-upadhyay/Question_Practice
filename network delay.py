import heapq
n=int(input())
e=int(input())
k=int(input())
times=[]
for _ in range(e):
    times.append(list(map(int,input().split())))
adj=[[] for _ in range(n)]
for u,v,w in times:
    adj[u-1].append((v-1,w))
heap=[]
dist=[float('inf')]*n
dist[k-1]=0
heapq.heappush(heap,(0,k-1))
def shortest(adj,heap,dist):
    while heap:
        di,sr=heapq.heappop(heap)
        if di>dist[sr]:
            continue
        for i in range(len(adj[sr])):
            nei=adj[sr][i][0]
            wei=adj[sr][i][1]
            if wei+di<dist[nei]:
                dist[nei]=wei+di
                heapq.heappush(heap,(wei+di,nei))
    print(dist)
    return max(dist) if max(dist)!=float('inf') not in dist else -1
print(shortest(adj,heap,dist))
