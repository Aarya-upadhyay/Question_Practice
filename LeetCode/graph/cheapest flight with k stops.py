n=int(input())
e=int(input())
src=int(input())
des=int(input())
k=int(input())
edges=[]
for i in range(e):
    edges.append(list(map(int,input().split())))
res=[float('inf')]*n
res[src]=0
def cheapest(edges,res):
    for i in range(k+1):
        new=res[:]
        for j in range(len(edges)):
            sr=edges[j][0]
            de=edges[j][1]
            we=edges[j][2]
            if res[sr]!=float('inf'):
                new[de]=min(new[de],res[sr]+we)
        res=new
    if res[des]!=float('inf'):
        return res[des]
    return [-1]
print(cheapest(edges,res))
        


