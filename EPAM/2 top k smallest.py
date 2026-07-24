"""ort heapq

n=int(input("enter the no of element"))
k=int(input("enter the k"))
heap=[]
op=[]
for _ in range(n):
    heapq.heappush(heap,int(input()))
for _ in range(k):
    c=heapq.heappop(heap)
    op.append(c)
print(op)
"""

import heapq as hp
n= int(input())
k=int(input())
op=[]
a=list(map(int,input().split()))
hp.heapify(a)
for _ in range(k):
    c=hp.heappop(a)
    op.append(c)
print(op)

