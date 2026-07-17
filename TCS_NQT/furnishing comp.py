c=input("enter the string")
l=int(input("enter the no of sets to be created out of c"))
A=[]
s=0
for _ in range(len(c)):
    if s<len(c):
        a=c[s:s+l]
        A.append(a)
        s=s+l
    else:
        break
if s!=len(c)-1:
    b=c[s:]
    A.append(b)
max_c=0
for i in A:
    cou=i.count('a')
    max_c=max(max_c,cou)
print(max_c)

