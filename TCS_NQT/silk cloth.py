n=int(input("enter the no of pairs"))
points=[]
s=set()
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
    s.add((x,y))
def codd(n,points,s):
    ans=4
    best=-1
    for i in range(n):
        x1,y1=points[i]
        for j in range(i+1,n):
            x2,y2=points[j]
            
            dx=x2-x1
            dy=y2-y1
            side=dx*dx+dy*dy
            c1=(x1-dx,y1+dy)
            d1=(x2-dx,y2+dy)
            need=0
            if c1 not in s:
                need+=1
            if d1 not in s:
                need+=1
            if need<ans or (need==ans and side<best):
                ans=need
                best=side
            need=0
            c2=(x1+dy,y1-dx)
            d2=(x2+dy,y2-dx)
            if c2 not in s:
                need+=1
            if d2 not in s:
                need+=1
            if need<ans or (need==ans and side<best):
                ans=need
                best=side
    return ans
d=codd(n,points,s)
print(d)
