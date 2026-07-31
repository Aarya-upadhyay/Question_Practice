n=int(input())
arr=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None
from collections import deque
root=Node(arr[0])
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

def check_sym(root1,root2):
    if root1 is None and root2 is None:
        return True 
    if root1 is None or root2 is None:
        return False
    if root1.val !=root2.val:
        return False
    
    r1=check_sym(root1.left,root2.right)
    r2=check_sym(root1.right,root2.left)
    if r1 and r2:
        return True
    else:
        return False
def symmetry(root):
    a=check_sym(root.left,root.right)
    return a

print(symmetry(root))
