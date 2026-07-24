import heapq
n=int(input())
k=int(input())
heap=[]
for i in range(n):
    heapq.heappush(heap,-(int(input())))
for _ in range(k-1):
    heapq.heappop(heap)
print(-heap[0])

