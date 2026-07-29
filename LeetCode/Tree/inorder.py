from collections import deque
n=int(input())
arr=list(map(int,input().split()))
class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None

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
ans=[]
def inordertraversal(root):
    if root is None:
        return ans
    inordertraversal(root.left)
    ans.append(root.val)
    print(root.val)
    inordertraversal(root.right)
a=inordertraversal(root)
print(a)

def preordertraversal(root):
    if root is None:
        return
    print(root.val,end=" ")
    preordertraversal(root.left)
    preordertraversal(root.right)
preordertraversal(root)

def postordertraversal(root):
    if root is None:
        return
    postordertraversal(root.left)
    postordertraversal(root.right)
    print(root.val,end=" ")
postordertraversal(root)
