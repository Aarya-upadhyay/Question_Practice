n=int(input("enter the no"))
a=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head=Node(a[0])
temp=head
for i in range(n):
    temp.next=Node(a[i])
    temp=temp.next

slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
print(slow.val)