"""n=int(input())
k=int(input())
arr=list(map(int,input().split()))
op=[]
for i in range(n):
    b=i+k
    if b<=n:
        a=arr[i:i+k]
        op.append(max(a))
print(op)"""

import heapq
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
heap=[]

for i in range(k):
    heapq.heappush(heap,(-arr[i],i))
ans=[-heap[[0][0]]]
for i in range(k,len(arr)):
    heapq.heappush(heap,(-arr[i],i))
    left=i-k+1
    if heap[0][1]<left:
        heapq.heappop(heap)
    ans.append(-heap[0][0])
print(ans)