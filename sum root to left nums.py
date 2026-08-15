n = int(input())
arr = input().split()

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if arr[0] != "null":
    root = Node(int(arr[0]))
else:
    root = None

from collections import deque

q = deque([root])
i = 1

while i < n and q:
    c = q.popleft()

    if i < n:
        if arr[i] != "null":
            c.left = Node(int(arr[i]))
            q.append(c.left)
        i += 1

    if i < n:
        if arr[i] != "null":
            c.right = Node(int(arr[i]))
            q.append(c.right)
        i += 1


def findsum(root):
    s=0
    def find(r,s,ar):
        if r is None:
            return 
        s+=str(r.val)
        if r.left is None and r.right is None:
            ar.append(s)
        find(r.left,s,ar)
        find(r.right,s,ar)
        return ar
    a=find(root,"",[])
    for i in a:
        s+=int(i)
    return s
print(findsum(root))

