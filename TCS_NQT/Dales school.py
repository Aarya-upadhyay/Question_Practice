n=int(input("enter the no of students"))
x=int(input("enter the index value on which you want to update"))
y=int(input("enter the value for x"))
arr=list(map(int,input().split()))
def cheater(n,x,y,arr):
    res=5
    arr[x-1]=y
    #res=[]
    #s=set()
    #s=set(arr)
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            res-=1
            #res.append(arr[i])
        #else:
            #s.add(arr[i])
    #fin=len(res)+len(s)
    #return fin


    return res
a=cheater(n,x,y,arr)
print(a)