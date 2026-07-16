s=input("enter the week day")
n=int(input("enter the no of days from the starting of weekday"))
def count_sundays(s,n):
    h={'mon':6,'tue':5,'wed':4,'thu':3,'fri':2,'sat':1,'sun':0}
    t=h[s]
    c_s=0
    while t<=n:
        c_s+=1
        t+=7
    return c_s

c=count_sundays(s,n)
print(c)


        