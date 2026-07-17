n=int(input("enter the no of elements"))
a=list(map(int,input("enter ").split()))
def prior(n,a):
    c=1
    for i in range(1,n):
        if a[i]>a[i-1]:
            c+=1
    return c
a1=prior(n,a)
print(a1)
