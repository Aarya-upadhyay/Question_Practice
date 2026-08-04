n=int(input())
arr=input().split()
m=int(input())
arr1=input().split()
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

if arr1[0]!="null":
    root1=Node(int(arr[0]))
else:
    rootq=None
from collections import deque
q1=deque([root1])
i=1
if root1 is None:
    print(None)
    exit()
while i<len(arr1) and q1:
    c=q1.popleft()
    if i<len(arr1):
        if arr1[i]!="null":
            c.left=Node(int(arr1[i]))
            q1.append(c.left)
        i+=1
    if i<len(arr1):
        if arr1[i]!="null":
            c.right=Node(int(arr1[i]))
            q1.append(c.right)
        i+=1


def issimilar(r,ans):
        if r is None:
            return
        
        
        
        if r.left is None and r.right is None:
            ans.append(r.val)
            print(ans)
            return ans
        issimilar(r.left,ans)
        issimilar(r.right,ans)

        
        
        
def leaf(root,root1):
    a=[]
    b=[]
    return (issimilar(root,a)==issimilar(root1,b))
   

print(leaf(root,root1))