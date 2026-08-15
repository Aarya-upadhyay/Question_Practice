class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

pos=list(map(int,input().split()))
ino=list(map(int,input().split()))

def construct(pos,ino):
    h={}
    for i in range(len(ino)):
        h[ino[i]]=i
    idx=len(pos)-1
    def func(pos,l,r):
        nonlocal idx
        if l>r or idx<0:
            return None
        node=Node(pos[idx])
        idx-=1
        i=h[node.val]
        node.right=func(pos,i+1,r)
        node.left=func(pos,l,i-1)
        
        return node
    return func(pos,0,len(pos)-1)
root=(construct(pos,ino))
def inorder(r):
    if r is None:
        return

    inorder(r.left)
    print(r.val, end=" ")
    inorder(r.right)


inorder(root)
