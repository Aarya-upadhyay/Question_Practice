n=int(input())
arr=[]
for _ in range(n):
    s=input()
    #arr.append(s.lower().strip())
    arr.append(s.lower().replace(" ",""))
h={}
for i in arr:
    h[i]=h.get(i,0)+1
for i,j in h.items():
    print((i,j),end='\n')