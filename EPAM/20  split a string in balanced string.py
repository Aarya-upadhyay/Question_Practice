s=input()
b=0
c=0
for i in s:
    if i=='R':
        b+=1
    else:
        b-=1
    if b==0:
        c+=1
print(c)