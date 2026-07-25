import heapq
from collections import Counter
arr=list(map(int,input().split()))
target=len(arr)//2
freq=Counter(arr)
heap=[]
for i in freq.values():
    heapq.heappush(heap,(-i))

rem=0
c=0
while rem<target:
    rem+=-heapq.heappop(heap)
    c+=1
print(c)
