n=int(input())
e=int(input())
src=int(input())
edges=[]
for _ in range(e):
    edges.append(list(map(int,input().split())))
res=[float('inf')]*n
res[src]=0
def bell(edges):
    for i in range(n-1):
        for j in range(len(edges)):
            sr=edges[j][0]
            di=edges[j][1]
            we=edges[j][2]
            if res[sr]!=float('inf') and res[di]>res[sr]+we:
                res[di]=res[sr]+we
bell(edges)
for j in range(len(edges)):
    sr=edges[j][0]
    di=edges[j][1]
    we=edges[j][2]
    if res[sr]!=float('inf') and res[di]>res[sr]+we:
        print([-1])
print(res)



