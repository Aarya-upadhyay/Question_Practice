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
from collections import deque
q=deque([root])
i=1
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

def maxsum(root):
    ans=float('-inf')
    def gain(r):
        nonlocal ans
        if r is None:
            return 0
        l=max(gain(r.left),0)
        r1=max(gain(r.right),0)
        ans=max(ans,r.val+l+r1)
        return r.val+max(l,r1)
    gain(root)
    return ans
print(maxsum(root))