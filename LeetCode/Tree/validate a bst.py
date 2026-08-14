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
"""
def findit(r,arr):
    if r is None:
        return arr
    findit(r.left,arr)
    arr.append(r.val)
    findit(r.right,arr)
    return arr

    

def validatebst(root):
    a=findit(root,[])
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            return False
        return True
print(validatebst(root))"""


prev=None
ans=True
def findif(root):
    global prev
    global ans
    if root is None:
        return 
    findif(root.left)
    if prev is None:
        prev=root

    else:
        if prev.val>=root.val:
            ans=False
        prev=root
    findif(root.right)
(findif(root))
print(ans)

        

        