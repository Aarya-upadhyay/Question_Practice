n=int(input())
arr=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

head=Node(arr[0])
t=head
for i in range(1,n):
    t.next=Node(arr[i])
    t=t.next

"""curr=head
prev=None
while curr:
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt
t=prev
while t:
    print(t.val,end=" ")
    t=t.next
"""

def recursive(head):
    """if head is None:
        return prev
    nxt=head.next
    head.next=prev
    prev=head
    head=nxt
    return recursive(head,prev)
    """

    if head is None or head.next is None:
        return head
    new_node=recursive(head.next)
    head.next.next=head
    head.next=None
    return new_node


   
t=recursive(head)
while t:
    print(t.val)
    t=t.next
