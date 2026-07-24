n=int(input())
a=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head=Node(a[0])
temp=head
for i in range(1,n):
    temp.next=Node(a[i])
    temp=temp.next

curr=head
prev=None
while curr:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
curr=prev
while curr:
    print(curr.val,end=" ")
    curr=curr.next
