n=int(input())
e=int(input())
graph=[[] for _ in range(n)]
rev=[[] for _ in range(n)]
out=[0]*n

for i in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)
    rev[v].append(u)
    out[u]+=1


from collections import deque
q=deque()
for i in range(n):
    if out[i]==0:
        q.append(i)
safe=[False]*n
while q:
    n=q.popleft()
    safe[n]=True
    for p in rev[n]:
        out[p]-=1
        if out[p]==0:
            q.append(p)

ans=[]
for i in range(n):
    if safe[i]:
        print(i)
        ans.append(i)
print(ans)
