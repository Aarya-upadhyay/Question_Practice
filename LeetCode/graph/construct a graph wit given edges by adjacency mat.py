edges=[]
n=int(input())
for _ in range(n):
    edges.append(list(map(int,input().split())))

vertices=max(max(e) for e in edges)+1
mat=[[0]*vertices for _ in range(vertices)]

for i in range(n):
    """e=edges[i]
    src=e[0]
    des=e[1]
    mat[src][des]=1
    mat[des][src]=1
    #if the graph is undirected graph
    """
    #if the grpah is directed
    """e=edges[i]
    src=e[0]
    des=e[1]
    mat[src][des]=1 
    """

    #if the graph is weighted
    e=edges[i]
    src=e[0]
    des=e[1]
    w=e[2]
    mat[src][des]=w
    
for i in range(len(mat)):
    print(mat[i])

