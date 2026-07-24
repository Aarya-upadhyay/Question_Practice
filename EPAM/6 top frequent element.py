import heapq
n=int(input())
k=int(input())
a=list(map(int,input().split()))
freq={}
for i in range(n):
    freq[a[i]]=freq.get(a[i],0)+1
heap=[]
for n,c in freq.items():
    heapq.heappush(heap,(-(c),-(n)))
op=[]
for i in heap:
    a,b=i
    op.append(-(b))
print(op[:k])

