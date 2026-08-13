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
    if i<n :
        if arr[i]!="null":
            c.left=Node(int(arr[i]))
            q.append(c.left)
        i+=1

    if i<n:
        if arr[i]!="null":
            c.right=Node(int(arr[i]))
            q.append(c.right)
        i+=1
q1=deque([root])

def findcbt(q1):
    nullfind=False
    while q1:
        t=q1.popleft()
        if t==None:
            nullfind=True
        else:
            if nullfind:
                return False
            q1.append(t.left)
            q1.append(t.right)
    return True
def cbt(root):
    return findcbt(q1)
print(cbt(root))
