arr=list(map(int,input().split()))
n=len(arr)
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def contruct(arr):
    def sft(l,r):
        if l>r:
            return None
        mid=(l+r)//2
        root=Node(arr[mid])
        root.left=sft(l,mid-1)
        root.right=sft(mid+1,r)
        return root
    return sft(0,n-1)
r1=contruct(arr)
def inorder(r1):
    if r1 is None:
        return
    print(r1.val)
    inorder(r1.left)
    inorder(r1.right)
inorder(r1)
