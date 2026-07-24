n=int(input())
k=int(input())
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
arr=list(map(int,input().split()))
head=Node(arr[0])
t=head
for i in range(1,n):
    t.next=Node(arr[i])
    t=t.next

"""t=head
prev=None
while t:
    nxt=t.next
    t.next=prev
    prev=t
    t.next=nxt

curr=prev
for i in range(k-2):
    curr=curr.next
curr.next=curr.next.next


t=curr
prev=None
while t:
    nxt=t.next
    t.next=prev
    prev=t
    t.next=nxt"""

dummy=Node(-1)
dummy.next=head
slow=dummy
fast=dummy
for _ in range(k+1):
    fast=fast.next

while fast:
    slow=slow.next
    fast=fast.next
slow.next=slow.next.next
t=dummy.next
while t:
    print(t.val,end=" ")
    t=t.next


