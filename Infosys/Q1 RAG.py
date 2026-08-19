n=int(input())
init=int(input())
power=[]
for i in range(n):
    power.append(int(input()))
bonus=[]
for i in range(n):
    bonus.append(int(input()))

"""c=0
visit=[0]*n
for _ in range(n):
    for i in range(n):
        if visit[i]==0:
            if init>=power[i]:
                c+=1
                init+=bonus[i]
                visit[i]=1
print(c)"""

a = sorted(zip(power, bonus)) 
ans = 0 
for powe, bonu in a: 
    if powe > init: 
        break 
    init += bonu 
    ans += 1 
print(ans)
