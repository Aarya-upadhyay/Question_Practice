n=int(input("enter no of elements"))
a=[]
for i in range(n):
    a.append(int(input("enter")))
l=0
m=0
h=n-1
while m<=h:
    if a[m]==0:
        a[l],a[m]=a[m],a[l]
        l+=1
        m+=1
    elif a[m]==1:
        m+=1
    else:
        a[m],a[h]=a[h],a[m]
        h-=1
for i in a:
    print(i,end=' ')
