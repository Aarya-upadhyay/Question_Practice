arr=list(map(int,input().split()))
target=int(input())
ans=[]
def backtrack(temp,idx,cs):
    if cs==target:
        ans.append(temp.copy())
        return
    if idx==len(arr):
        return
    if cs>target:

        return
    """ktrack(temp,idx+1,cs)
    temp.append(arr[idx])
    backtrack(temp,idx+1,cs+arr[idx])
    temp.pop()"""

    # Take current element (can reuse it)
    temp.append(arr[idx])
    backtrack(temp,idx, cs+arr[idx])
    temp.pop()

    # Skip current element
    backtrack(temp,idx+1,cs)
backtrack([],0,0)
print(ans)