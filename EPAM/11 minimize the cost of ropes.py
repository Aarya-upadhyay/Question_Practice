"""n=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum=arr[0]+arr[1]
total=sum
for i in range(2,n):
    sum+=arr[i]
    total+=sum
print(total)"""
import heapq
n=int(input())
heap=[]
arr=list(map(int,input().split()))
for i in range(n):
    heapq.heappush(heap,arr[i])
total=0
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    sum=a+b
    total+=sum
    heapq.heappush(heap,sum)
print(total)