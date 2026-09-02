n=int(input())
h={}
def fin(n):
    if n==0 or n==1:
        return n
    if n in h:
        return h[n]
    a1=fin(n-1)
    a2=fin(n-2)
    ans=a1+a2
    h[n]=ans
    return ans
f=fin(n)
print(f)


def tabulation(n):
    ar=[-1]*(n+1)
    if n==0 or n==1:
        return 0
    ar[0]=0
    ar[1]=1
    for i in range(2,n+1):
        ar[i]=ar[i-1]+ar[i-2]
    return ar[n]
print(tabulation(n))


def spaceoptimization(n):
    prev=1
    prev_p=0
    for i in range(1,n):
        ans=prev+prev_p
        prev_p=prev
        prev=ans
    return ans
print(spaceoptimization(n))
