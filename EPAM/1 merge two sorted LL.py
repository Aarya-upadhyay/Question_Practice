n=int(input("enter the no of elements in list1"))
m=int(input("enter the no of elements in list2"))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a1=list(map(int,input().split()))
list1=Node(a1[0])
curr=list1
for i in range(1,n):
    curr.next=Node(a1[i])
    curr=curr.next
       
a2=list(map(int,input().split()))
list2=Node(a2[0])
curr=list2
for i in range(1,m):
    curr.next=Node(a2[i])
    curr=curr.next

dummy=Node(-1)
curr=dummy
while list1 and list2:
    if list1.data<=list2.data:
        curr.next=list1
        list1=list1.next
        
    else:
        curr.next=list2
        list2=list2.next
    curr=curr.next
       
curr.next=list1 if list1 else list2
temp=dummy.next
while temp:
    print(temp.data,end=" ")
    temp=temp.next
