n=int(input())
k=int(input())
def counter(n,k):
    num=0
    if k==1:
        return n
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j%i==0:
                    num+=1
    return num
print(counter(n,k))