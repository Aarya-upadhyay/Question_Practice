n=int(input("enter the no"))
A=list(map(int,input().split()))
even=0
odd=0
for i in range(n):
    if i%2==0:
        even+=A[i]
    else:
        odd+=A[i]
if even>odd:
    print(even)
else:
    print(odd)