n=int(input())
arr=input().split()
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
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
"""def findd(r,c):
    if r is None:
        return 0
    c+=1
    print(c)
    if r.left is None and r.right is None:
        return c
    findd(r.left,c)
    findd(r.right,c)
    return c
    
def finddiameter(root):
    r1=findd(root.left,0)
    r2=findd(root.right,0)
    print(r1+r2)
print(finddiameter(root))"""
res=0
def find(root):
    global res
    if root is None:
        return 0
    left=find(root.left)
    right=find(root.right)
    sum=left+right
    res=max(res,sum)
    return 1+max(left,right)
print(find(root))
    