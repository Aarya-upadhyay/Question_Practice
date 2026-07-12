n=int(input("enter the no of horses"))
k=int(input("enter the money bob had"))
p=[]
for i in range(n):
    x=int(input('enter'))
    p.append(x)
print(p)
l=0
money=0
res=float('-inf')
for i in range(n):
    money+=p[i]
    while money>=k:
        money-=p[l]
        l+=1
    res=max(res,i-l+1)
print(res)



