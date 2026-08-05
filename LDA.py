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
from collections import deque
q=deque([root])
i=1
if root is None:
    print(None)
    exit()
while i<len(arr) and q:
    c=q.popleft()
    if i<len(arr):
        if arr[i]!="null":
            c.left=Node(int(arr[i]))
            q.append(c.left)
        i+=1
    if i<len(arr):
        if arr[i]!="null":
            c.right=Node(int(arr[i]))
            q.append(c.right)
        i+=1

ans=None
def LDA(root,p,q):
    if root is None:
        return 0
    l=LDA(root.left,p,q)
    r=LDA(root.right,p,q)
    self1=0
    if root.val==p or root.val==q:

        self1=1
    total=l+self1+r
    if total==2:
        return 2
    return total
p=int(input())
q=int(input())
print(LDA(root,p,q))