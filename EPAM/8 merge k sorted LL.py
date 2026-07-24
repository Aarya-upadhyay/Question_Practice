import heapq
k=int(input())
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def createLL(arr):
    head=Node(arr[0])
    t=head
    for i in range(1,len(arr)):
        t.next=Node(arr[i])
        t=t.next
    return head

lists=[]
for i in range(k):
    n=int(input())
    arr=list(map(int,input().split()))
    head=createLL(arr)
    lists.append(head)


heap=[]
for i in range(k):
    if lists[i]:
        heapq.heappush(heap,(lists[i].val,i,lists[i]))
dummy=Node(-1)
c=dummy
while heap:
    value,index,node=heapq.heappop(heap)
    c.next=node
    c=c.next
    if node.next:
        heapq.heappush(heap,(node.next.val,index,node.next))

printList(dummy.next)