arr=list(map(int,input().split()))
n=len(arr)
dp=[[-1,-1]]*n
print(dp)
def maxrob(arr,n,i,free,dp):
    if i==n:
        return 0
    if free==0:
        dp[i][free]=maxrob(arr,n,i+1,1,dp)
        return dp[i][free]
    c1=arr[i]+maxrob(arr,n,i+1,0,dp)
    c2=maxrob(arr,n,i+1,1,dp)
    dp[i][free]=max(c1,c2)
    return dp[i][free]
r=maxrob(arr,n,0,1,dp)
print(r)


# tc - O(n) sc- O(n+2)= O(n)
def tabulation(arr,n):
    dp=[-1]*(n+2)
    dp[n]=0
    dp[n+1]=0
    for i in range(n-1,-1,-1):
        take=arr[i]+dp[i+2]
        dont=dp[i+1]
        dp[i]=max(take,dont)
    return dp[0]
print(tabulation(arr,n))

#TC- O(n) SC= O(1)
def spaceoptimization(arr,n):
    nxt=0
    n_nxt=0
    max_curr=0
    for i in range(n-1,-1,-1):
        curr=arr[i]+n_nxt
        do=nxt
        max_curr=max(curr,do)
        n_nxt=nxt
        nxt=max_curr
    return max_curr
print(spaceoptimization(arr,n))
