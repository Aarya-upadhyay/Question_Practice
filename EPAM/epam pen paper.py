n,k,c=map(int,input().split())
arr=list(map(int,input().split()))
l=0
ans=0
co=0
for i in range(2*n):
    if arr[i%n]>c:
        co+=1
    while co>k or i-l+1>n:
        if arr[l%n]>c:
            co-=1
        l+=1
    if co==k:
        ans=max(ans,i-l+1)
print(ans)



#2nd approach because of which i wasnt shortlisted dude

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

head=Node(arr[0])
t=head
for i in range(1,n):
    t.next=Node(arr[i])
    t=t.next
t.next=head
l=head
r=head
ans=0
co=0
win=0
for _ in range(2*n):
    win+=1
    if r.val>c:
        co+=1
    r=r.next
    while co>k or win>n:
        if l.val>c:
            co-=1
        win-=1
        l=l.next
    if co==k:
        anx=max(ans,win)
print(ans)




