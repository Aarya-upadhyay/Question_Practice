a=input("enter the string A")
b=input("enter the string B")
def st(a,b):
    res=""
    for i in a:
        if i not in b:
            res+=i
    return res
print(st(a,b))