arr=list(map(int,input().split()))
n=len(arr)
arr1=list(map(int,input().split()))
m=len(arr1)
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=Node(arr[0])
root1=Node(arr1[0])
from collections import deque
q=deque([root])
qu=deque([root1])

i=1 
while i<n and q:
    c=q.popleft()
    if i<n:
        c.left=Node(arr[i])
        q.append(c.left)
        i+=1
    if i < n:
        c.right=Node(arr[i])
        q.append(c.right)
        i+=1

i=1 
while i<m and qu:
    c=qu.popleft()
    if i<n:
        c.left=Node(arr1[i])
        qu.append(c.left)
        i+=1
    if i < m:
        c.right=Node(arr1[i])
        qu.append(c.right)
        i+=1
    

    
def findequivalent(root,root1):
    if root is None and root1 is None:
        return True
    if root is None or root1 is None:
        return False
    if root.left==root1.right and root.right==root1.left:
        return True
    r1=findequivalent(root.left,root.right)
    r2=findequivalent(root.right,root1.left)
    if r1 or r2:
        return True
    else:
        return False
print(findequivalent(root,root1))

