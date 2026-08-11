n=int(input())
arr=input().split()
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
if arr[0]!="null":
    root=Node(int(arr[0]))
else:
    root=None
from collections import deque
q=deque([root])
i=1
while i<n and q:
    c=q.popleft()
    if i<n:
        if arr[i]!="null":
            c.left=Node(int(arr[i]))
            q.append(c.left)
        i+=1
    if i<n:
        if arr[i]!="null":
            c.right=Node(int(arr[i]))
            q.append(c.right)
        i+=1

def mindepth(root,m,c):
    if root is None:
        return 0
    m+=1
    if root.left is None and root.right is None:
        c=min(c,m)
        return c
    c=mindepth(root.left,m,c)
    c=mindepth(root.right,m,c)
    return c
c=float('inf')
print(mindepth(root,0,c))