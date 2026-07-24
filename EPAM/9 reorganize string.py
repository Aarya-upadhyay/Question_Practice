"""import heapq
s=input()
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
heap=[]
for ch,co in freq.items():
    heapq.heappush(heap,(-co,ch))
prev=(0,"")
ans=[]
while heap:
    co,ch=heapq.heappop(heap)
    ans.append(ch)
    if prev[0]<0:
        heapq.heappush(heap,prev)
    co+=1
    prev=(co,ch)
res="".join(ans)
if len(res)!=len(s):
    print("")
else:
    print(res)"""

from collections import Counter
def reorganize(s):
    freq=Counter(s)
    n=len(s)
    max_ch=max(freq,key=freq.get)
    if freq[max_ch]>(n+1)//2:
        return ""
    ans=[""]*n
    index=0
    while freq[max_ch]:
        ans[index]=max_ch
        index+=2
        freq[max_ch]-=1
    for ch in freq:
        while freq[ch]:
            if index>=n:
                index=1
            ans[index]=ch
            index+=2
            freq[ch]-=1
    return "".join(ans)
a=reorganize("aaabbc")
print(a)
