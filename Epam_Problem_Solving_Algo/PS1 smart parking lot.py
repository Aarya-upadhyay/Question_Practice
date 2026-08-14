E=int(input())
class Node:
    def __init__(self,val,time):
        self.val=val
        self.time=time
        self.next=None
head=None
tail=None
for _ in range(E):
    v,t=input().split()
    node=Node(v,int(t))
    if head is None:
        head=node
        tail=node
    else:
        tail.next=node
        tail=node


S=int(input())
freq={}
for i in range(S):
    
    v,al=input().split()
    freq[v]=int(al)
t=head
count={}

while t:
    count[t.val]=count.get(t.val,0)+1
    t=t.next




ans=[]
for v,ac in freq.items():
    a=count.get(v,0)
    if a>ac:
        ex=a-ac
        ans.append((ex,v))
for i in ans:
    print(i)




