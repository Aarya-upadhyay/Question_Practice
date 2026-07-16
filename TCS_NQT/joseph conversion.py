n=int(input("enter the decimal no"))
temp=n
bits=0
while temp:
    bits+=1
    temp//=2
mask=(1<<bits)-1
print( n^mask)