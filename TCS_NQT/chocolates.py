n=int(input("ENter the no of packates"))
#A=[]
#for _ in range(n):
#   A.append(int(input()))
def chocolates(n,A):
    j=0
    for i in range(n):
        if A[i]!=0:
            A[i],A[j]=A[j],A[i]
            j+=1
    return A
#a=chocolates(n,A)

j=0
A=[0]*n
for i in range(n):
    a=int(input())
    if a!=0:
        A[j]=a
        j+=1
for i in A:
    print(i,end=" ")

