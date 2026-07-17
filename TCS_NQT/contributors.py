n=int(input("enter the day"))
a=list(map(int,input().split()))
x=int(input("enter fine"))
c=0
if n%2==0:
    for i in a:
        if i%2!=0:
            c+=1
else:
    for i in a:
        if i%2==0:
            c+=1
print(c*x)