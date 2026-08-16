n=int(input("enter no of ver"))
m=int(input("enter no of edges"))
edges=[]
for _ in range(m):
    edges.append(list(map(int,input().split())))
adj=[[] for i in range(n)]
for i in range(n):
    e=edges[i]
    src=e[0]
    des=e[1]
  
    adj[src].append(des)
    adj[des].append(src)

for i in range(len(adj)):
    print(adj[i])