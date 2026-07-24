import heapq
n=int(input())
k=int(input())
l=[]
for i in range(n):
    arr=list(map(int,input().split()))
    l.append(arr)

heap=[]
for x,y in l:
    d=(x*x+y*y)**0.5
    heapq.heappush(heap,(d,[x,y]))

op=[]
for _ in range(k):
    d,p=heapq.heappop(heap)
    op.append(p)
print(op)