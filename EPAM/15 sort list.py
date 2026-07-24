n=int(input())
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
arr=list(map(int,input().split()))
head=Node(arr[0])
h=head
for i in range(1,n):
    h.next=Node(arr[i])
    h=h.next
"""h=head
l=[]
while h:
    l.append(h.val)
    h=h.next

l.sort()
head1=Node(l[0])
h=head1
for i in range(1,n):
    h.next=Node(l[i])
    h=h.next

h=head1
while h:
    print(h.val,end=" ")
    h=h.next
    """



def findmid(head):
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
    return slow


def merge(left,right):
    dummy=Node(-1)
    tail=dummy
    while left and right:
        if left.val<=right.val:
            tail.next=left
            left=left.next
        else:
            tail.next=right
            right=right.next
        tail=tail.next
    if left:
        tail.next=left
    else:
        tail.next=right
    return dummy.next


def sortlist(head):
    if head is None or head.next is None:
        return head
    mid=findmid(head)
    right=mid.next
    mid.next=None
    left=head
    left=sortlist(left)
    right=sortlist(right)
    return merge(left,right)

def printList(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()

head=sortlist(head)
printList(head)
    
