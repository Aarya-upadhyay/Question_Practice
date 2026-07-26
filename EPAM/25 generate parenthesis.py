n=int(input())
ans=[]
def backtrack(c,op,cl):
    if len(c)==2*n:
        ans.append(c)
        return
    if op<n:
        backtrack(c+"(",op+1,cl)
    if cl<op:
        backtrack(c+")",op,cl+1)
backtrack("",0,0)
print(ans)