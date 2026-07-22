class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input())
arr=list(map(int,input().split()))
head=Node(arr[0])
curr=head
for i in range(1,n):
    curr.next=Node(arr[i])
    curr=curr.next
slow=head
fast=head
while fast.next and fast.next.next:
    slow=slow.next
    fast=fast.next.next
print(slow.data)