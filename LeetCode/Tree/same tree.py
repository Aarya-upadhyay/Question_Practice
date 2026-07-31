n=int(input())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
from collections import deque
root1=Node(arr[0])
q1=deque([root1])
i=1
while i<n and q1:
    curr=q1.popleft()
    if i<n:
        curr.left=Node(arr[i])
        q1.append(curr.left)
        i+=1
    if i<n:
        curr.right=Node(arr[i])
        q1.append(curr.right)
        i+=1

root2=Node(arr1[0])
q2=deque([root2])
i=1
while i<n and q2:
    curr=q2.popleft()
    if i<n:
        curr.left=Node(arr1[i])
        q2.append(curr.left)
        i+=1
    if i<n:
        curr.right=Node(arr1[i])
        q2.append(curr.right)
        i+=1

def issame(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val!=root2.val:
        return False
    r1=issame(root1.left,root2.left)
    r2=issame(root1.right,root2.right)
    if r1 and r2:
        return True
    else:
        return False

print(issame(root1,root2))

