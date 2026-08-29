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