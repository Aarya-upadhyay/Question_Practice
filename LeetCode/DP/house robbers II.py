arr=list(map(int,input().split()))
n=len(arr)
def fun(arr):
    dp=[[-1,-1] for _ in range(n)]
    if n==1:
        return arr[0]
    def rec(arr,n,i,free,dp):
        if i==n:
            return 0
        if dp[i][free]!=-1:
            return dp[i][free]
        if free==0:
            dp[i][free]=rec(arr,n,i+1,1,dp)
            return dp[i][free]
        c1=arr[i]+rec(arr,n,i+1,0,dp)
        c2=rec(arr,n,i+1,1,dp)
        dp[i][free]=max(c1,c2)
        return dp[i][free]
    return rec(arr,n,0,1,dp)
case1=fun(arr[1:])
case2=fun(arr[:-1])
print(max(case1,case2))

def tabulation(arr):
    n=len(arr)
    dp=[-1]*(n+2)
    dp[n]=0
    dp[n+1]=0
    for i in range(n-1,-1,-1):
        take=arr[i]+dp[i+2]
        dont=dp[i+1]
        dp[i]=max(take,dont)
    return dp[0]
a1=tabulation(arr[1:])
a2=tabulation(arr[:-1])
print(max(a1,a2))


def space(arr):
    n=len(arr)
    nxt=0
    n_nxt=0
    for i in range(n-1,-1,-1):
        take=arr[i]+n_nxt
        dont=nxt
        n_nxt=nxt
        nxt=max(dont,take)
    return nxt
a1=space(arr[1:])
a2=space(arr[:-1])
print(max(a1,a2))
