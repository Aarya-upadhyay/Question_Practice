n=int(input())
def rec(n):
    if n==1:
        return True
    if n<=0 or n%2!=0:
        return False
    return rec(n//2)
t=rec(n)
print(t)