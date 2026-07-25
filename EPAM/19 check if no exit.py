from collections import Counter
arr=list(map(int,input().split()))

freq=Counter(arr)
"""for i in arr:
    if i==0 or i==1:
        continue
    freq[i]=i*2
exist=0
for sq in freq.values():
    if sq in arr:
        exist=1
if exist:
    print("true")
else:
    print("false")
    """
for i in freq:
    if i==0:
        if freq[i]>1:
            print("Trrue")
            break
    elif i*2 in arr:
        print("True")
        break
else:print("False")