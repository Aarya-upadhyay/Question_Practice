import heapq
prio={}
n=int(input())
for _ in range(n):
    cus,sev=input().split()
    sev=int(sev)
    if cus not in prio:
        prio[cus]=sev
    else:
        prio[cus]=max(prio[cus],sev)

heap=[]
for c,s in prio.items():
    heapq.heappush(heap,(-s,c))
ans=[]
while heap:
    a=heapq.heappop(heap)[1]
    ans.append(a)
print(ans)