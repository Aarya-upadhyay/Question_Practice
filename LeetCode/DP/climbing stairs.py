n=int(input())
h={}
def climbing(n,i):
    if i==n:
        return 1
    if i>n:
        return 0
    if i in h:
        return h[i]
    a1=climbing(n,i+1)
    a2=climbing(n,i+2)
    ans=a1+a2
    h[i]=ans
    return ans
c=climbing(n,0)
print(c)

ar=[-1]*(n+2)
def tabulation(n,i):
    ar[n]=1
    ar[n+1]=0
    for i in range(n-1,-1,-1):
        ar[i]=ar[i+1]+ar[i+2]
    return ar[0]
print(tabulation(n,0))


def spaceoptimized(n,i):
    one=1
    two=0
    for i in range(n-1,-1,-1):
        curr=one+two
        two=one
        one=curr
    return curr
print(spaceoptimized(n,0))
