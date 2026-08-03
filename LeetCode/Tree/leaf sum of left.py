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

def leaf(r):
    if r is None:
        return 0
    s=0
    if r.left and (r.left.left is None and r.left.right is None) :
        s=r.left.val
        
    return s+leaf(r.left)+leaf(r.right)
def find(root):
    return leaf(root)
print(find(root))
