import heapq
from collections import Counter
n=int(input())
k=int(input())
words=list(map(str,input().split()))

freq=Counter(words)
heap=[]
for w,f in freq.items():
    heapq.heappush(heap,(-f,w))
op=[]
for i in range(k):
    a,b=heapq.heappop(heap)
    op.append(b)
print(op)



