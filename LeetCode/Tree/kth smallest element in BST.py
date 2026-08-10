n=int(input())
import heapq
arr=input().split()
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
if arr[0]!="null":
    root=Node(int(arr[0]))
else:
    root=None
i=1
from collections import deque
q=deque([root])
while i<n and q:
    c=q.popleft()
    if i<n:
        if arr[i]!="null":
            c.left=Node(int(arr[i]))
            q.append(c.left)
        i+=1
    if i<n:
        if arr[i]!="null":
            c.right=Node(int(arr[i]))
            q.append(c.right)
        i+=1


def kth(r,k,heap):
    if r is None:
        return False
    heapq.heappush(heap,r.val)
    kth(r.left,k,heap)
    kth(r.right,k,heap)
    return heap
def findit(root,k):
    heap=[]
    r=kth(root,k,heap)
    for i in range(k-1):
        heapq.heappop(heap)
    return heap[0]
k=int(input())
print(findit(root,k))