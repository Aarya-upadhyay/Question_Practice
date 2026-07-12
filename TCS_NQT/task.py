n=9
a=[-1,18,13,18,2,16,-1,-213,11]
def fair_sequence(a,n):
    sum1=0
  
    t=0
    while t<n:
        if a[t]>0:
            max_pos=float('-inf')

        
            while t<len(a) and a[t]>0 :
                max_pos=max(max_pos,a[t])
                t+=1
            sum1+=max_pos
        else:
            max_neg=float('inf')
            while  t<len(a) and a[t]<0:
                max_neg=max(max_neg,a[t])
                t+=1
            sum1=max_neg
    return sum1
c=fair_sequence(a,n)
print(c)