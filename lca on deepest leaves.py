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
def dfs(r):
    if r is None:
        return (0,None)
    left_depth,left_node=(dfs(r.left))
    right_depth,right_node=dfs(r.right)
    if left_depth>right_depth:
        return (left_depth+1,left_node)
    elif left_depth<right_depth:
        return(right_depth+1,right_node)
    else:
        return(left_depth+1,r) 
  
    
def lcaofdeepestleaves(root):
    depth,ans=dfs(root)
    return ans.val
print(lcaofdeepestleaves)
