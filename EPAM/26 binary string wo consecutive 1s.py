n=int(input())
ans=[]
def backtrack(c,idx):
    if idx==n:
        ans.append(c)
        return
    

    backtrack(c+"0",idx+1)
    if not c or c[-1]!="1":
        backtrack(c+"1",idx+1)
backtrack("",0)
print(ans)
