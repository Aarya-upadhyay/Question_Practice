n=int(input())
arr=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque
root=Node(arr[0])
q=deque([root])
i=1


while q and i<n:
    curr=q.popleft()
    if i<n:
        curr.left=Node(arr[i])
        q.append(curr.left)
        i+=1
    if i<n:
        curr.right=Node(arr[i])
        q.append(curr.right)
        i+=1

def levelorder(qu):
    rea=[]
    while qu :
        size=len(qu)
        arr=[]
        while size:
            t=qu.popleft()
            arr.append(t.val)
            if t.left :
                qu.append(t.left)
            if t.right :
                qu.append(t.right)
            size-=1
        rea.append(arr)

    return rea

qu=deque([root])
a=levelorder(qu)
print(a)
    

