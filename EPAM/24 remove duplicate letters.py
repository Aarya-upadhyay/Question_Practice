from collections import Counter
s=input()
freq=Counter(s)
set1=set()
stack=[]
for ch in s:
    freq[ch]-=1
    if ch in set1:
        continue

    while (stack and stack[-1]>ch and freq[stack[-1]]>0):
        set1.remove(stack.pop())
  
    stack.append(ch)
    set1.add(ch)

print("".join(stack))
    