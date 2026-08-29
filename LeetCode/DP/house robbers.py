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