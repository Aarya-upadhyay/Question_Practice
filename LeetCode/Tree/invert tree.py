n=int(input())
arr=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=Node(arr[0])
from collections import deque
q=deque([root])
i=1
while i<n and q:
    c=q.popleft()
    if i<n:
        c.left=Node(arr[i])
        q.append(c.left)
        i+=1
    if i<n:
        c.right=Node(arr[i])
        q.append(c.right)
        i+=1

def invert(root):
    if root is None:
        return None
    root.left,root.right=root.right,root.left
    invert(root.left)
    invert(root.right)
    return root
#print(invert(root))
r=invert(root)
qu=deque([root])
arr=[]
while qu:
    c=qu.popleft()
    print(c.val,end=" ")
    if c.left:
        qu.append(c.left)
    if c.right:
        qu.append(c.right)


