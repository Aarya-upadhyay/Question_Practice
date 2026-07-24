n=int(input("enter the no of ele"))
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

temp=head
while temp and temp.next:
    if temp.val==temp.next.val:
        temp.next=temp.next.next
    temp=temp.next
temp=head
while temp:
    print(temp.val,end=" ")
    temp=temp.next