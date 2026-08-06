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
    root =None
from collections import deque
i=1
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

def psum(r, temp, ans, s, targetsum):
    if r is None:
        return

    temp.append(r.val)
    s += r.val

    if r.left is None and r.right is None:
        if s == targetsum:
            ans.append(temp.copy())
    else:
        psum(r.left, temp, ans, s, targetsum)
        psum(r.right, temp, ans, s, targetsum)

    temp.pop()
def mainfunc(root, targetsum):
    ans = []
    psum(root, [], ans, 0, targetsum)
    return ans
targetsum=int(input())
print(mainfunc(root,targetsum))

        
        

