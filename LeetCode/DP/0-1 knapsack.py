val=list(map(int,input().split()))
wt=list(map(int,input().split()))
w=int(input())
n=len(val)
dp=[[-1]* (w+1) for _ in range(n)]
def fun(val,wt,n,i,w,dp):
    if i==n:
        return 0
    if dp[i][w]!=-1:
        return dp[i][w]
    if wt[i]>w:
        dp[i][w]=fun(val,wt,n,i+1,w,dp)
        return dp[i][w]
    yes=val[i]+fun(val,wt,n,i+1,w-wt[i],dp)
    no=fun(val,wt,n,i+1,w,dp)
    dp[i][w]=max(yes,no)
    return dp[i][w]
t=fun(val,wt,n,0,w,dp)
print(t)
        