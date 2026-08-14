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

i=1
from collections import deque
q=deque([root])
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
"""
def findceilandfloor(root,arr):
    if root is None:
        return arr
    findceilandfloor(root.left,arr)
    arr.append(root.val)
    findceilandfloor(root.right,arr)
    return arr
a=findceilandfloor(root,[])
x=int(input())
a.append(x)
a.sort()
f,c=-1,-1
for i in range(1,len(arr)-1):
    if a[i-1]<x and a[i+1]>x:
        f=a[i-1]
        c=a[i+1]

if f==-1 or c==-1:
    print(-1,-1)
else:
    print(f,c)
f,c=-1,-1
for v in a:
    if v<=x:
        f=v
    elif v>x:
        c=v
        break

print(f,c)
"""
x=int(input())
def find(root):
    f=-1
    c=-1
    while root:
        if root.val==x:
            f=root.val
            c=root.val
        elif root.val<x:
            f=root.val
            root=root.right
        else:
            c=root.val
            root=root.left
    return (f,c)
print(find(root))
    