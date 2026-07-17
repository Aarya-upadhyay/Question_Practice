n=int(input("enter the num"))
r=int(input("no of repition0"))
s=0
while r:
    a=n
    while n:
        d=n%10
        s+=d
        n//=10
    r-=1
ans=0
while s:
    a=s%10
    ans+=a
    s//=10
print(ans)