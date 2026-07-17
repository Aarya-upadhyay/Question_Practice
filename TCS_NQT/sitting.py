n=int(input("enter the members"))
def fact(n):
    p=1
    while n:
        p*=n
        n-=1
    return p
def sitting(n):
    a=fact(n-1)
    ans=a*2
    return ans
s=sitting(n)
print(s)