import heapq
k=int(input())
wages=list(map(int,input().split()))
quality=list(map(int,input().split()))
ratio=[]
for i in range(len(wages)):
    ratio.append(((wages[i]/quality[i]),quality[i]))
ratio.sort()
heap=[]
t_q=0
ans=float('inf')
for r,q in ratio:
    heapq.heappush(heap,(-q))
    t_q+=q
    if len(heap)>k:
        rem=-heapq.heappop(heap)
        t_q-=rem
    if len(heap)==k:
        cost=r*t_q
        ans=min(ans,cost)
print(ans)