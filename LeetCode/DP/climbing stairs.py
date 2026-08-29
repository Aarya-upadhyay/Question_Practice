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