from collections import defaultdict
arr=list(map(str,input().split()))
group=defaultdict(list)
for word in arr:
    key="".join(sorted(word))
    group[key].append(word)
print((group.values()))