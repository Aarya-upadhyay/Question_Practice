arr=input().split()
n=len(arr)
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

if arr[0]!='null':
    root=Node(int(arr[0]))
else:
    root=None

from collections import deque
q=deque([root])
i=1
while q and i<n:
    c=q.popleft()
    if i<n:
        if arr[i]!='null':
            c.left=Node(int(arr[i]))
            q.append(c.left)
        i+=1
    if i<n:
        if arr[i]!='null':
            c.right=Node(int(arr[i]))
            q.append(c.right)
        i+=1


def bt(root):
    if root is None:
        return None
    q1=deque([root])
    ar=[]
    while q1:
        for _ in range(len(q1)):
            c=q1.popleft()
            
            if c.left:
                q1.append(c.left)
            if c.right:
                q1.append(c.right)
        ar.append(c.val)
    return ar
print(bt(root))