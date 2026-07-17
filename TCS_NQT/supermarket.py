n=int(input("enter the amount"))
def price(n):
    p=1
    while n:
        d=n%10
        p*=d
        n//=10
    return p
a=price(n)
print(a)