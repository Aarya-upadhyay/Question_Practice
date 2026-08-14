list1=[]
n=int(input())
for i in range(n):
    a=list(map(str,input().split()))
    list1.append(a)

list2=[]
m=int(input())
for i in range(m):
    a=list(map(str,input().split()))
    list1.append(a)
lists=list1+list2
print(lists)
hashmap={}
for i in lists:
    a=i[0]
    b=int(i[1])
    if a in hashmap:
        hashmap[a]+=b
    else:
        hashmap[a]=b

for i,j in hashmap.items():
    if j==0:
        print("EMPTY")
        break
    print((i,j))

