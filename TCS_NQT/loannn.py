p=int(input("enter Principle"))
t=int(input("enter tenure"))
n1=int(input("bank a's slabs"))
N1=[]
for i in range(n1):
    x,y=map(float,input().split())
    N1.append((x,y))

n2=int(input("bank b's slabs"))
N2=[]
for i in range(n2):
    x,y=map(float,input().split())
    N2.append((x,y))


sum_emi_A=0
for i in range(n1):
    x,y=N1[i]
    emi=(p*y)/(1-1/(1+y)**(x*12))
    sum_emi_A+=emi

sum_emi_B=0
for i in range(n2):
    x,y=N2[i]
    emi=(p*y)/(1-1/(1+y)**(x*12))
    sum_emi_B+=emi

if sum_emi_A>sum_emi_B:
    print("Bank A")
else:
    print("Bank B")