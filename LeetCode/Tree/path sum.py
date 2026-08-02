n=int(input())
arr=list(map(str,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

if arr[0]=="null":
    root=None
else:
    root=Node(int(arr[0]))


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
su=0
def sump(r,t,su):
    if r is None:
        return False
    su+=r.val
    print(r.val,t,su)
    if r.left is None and r.right is None:
        print("yes")
        return su==t
        
    return (sump(r.left,t,su) or sump(r.right,t,su))
    
    
def pathsum(root,target):
    return sump(root,target,0)
target=int(input())
print(pathsum(root,target))

    