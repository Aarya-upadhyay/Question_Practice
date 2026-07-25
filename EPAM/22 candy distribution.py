candy=list(map(int,input().split()))
n=len(candy)
op=[1]*n
for i in range(1,n):
    if candy[i]>candy[i-1]:
        op[i]=op[i-1]+1
for i in range(n-2,-1,-1):
    if candy[i]>candy[i+1]:
        op[i]=max(op[i],op[i+1]+1)
print(sum(op))