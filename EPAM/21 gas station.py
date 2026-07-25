gas=list(map(int,input().split()))
cost=list(map(int,input().split()))
n=len(gas)
m=len(cost)
start=0
tank=0
total=0
for i in range(n):
    gain=gas[i]-cost[i]
    tank+=gain
    total+=gain
    if tank<0:
        start=i+1
        tank=0
if total>=0:
    print(start)
else:
    print(-1)
