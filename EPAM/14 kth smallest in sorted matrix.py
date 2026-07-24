n=int(input())
k=int(input())
l=[]
for i in range(k):
    a=list(map(int,input().split()))
    l.append(a)
import heapq
heap=[]
for r in range(n):
    heapq.heappush(heap,(l[r][0],r,0))
for _ in range(k-1):
    v,r,c=heapq.heappop(heap)
    if c+1<n:
        heapq.heappush(heap,(l[r][c+1],r,c+1))
print(heapq.heappop(heap)[0])
