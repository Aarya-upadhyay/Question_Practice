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
x=int(input())
def remove(head,x):
    t=head
    if head is None:
        return None
    while head and head.val==x:
        head=head.next
    t=head
    while t and t.next:
        if t.next.val==x:
            t.next=t.next.next
        else:
            t=t.next
    return head
p=(remove(head,x))
t=p
while t:
    print(t.val,end=" ")
    t=t.next


def recursive(head,x):
    if head is None:
        return None
    if head.val==x:
        head=head.next
    if head.next and head.next.val==x:
        head.next=head.next.next
    recursive(head.next,x)
    return head
q=recursive(head,x)
t=q

while t:
    print(t.val,end=" ")
    t=t.next


    