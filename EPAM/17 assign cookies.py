n=int(input())
m=int(input())
greed=list(map(int,input().split()))
size=list(map(int,input().split()))
greed.sort()
size.sort()

i = 0   # child pointer
j = 0   # cookie pointer

count = 0

while i < n and j < m:

    if size[j] >= greed[i]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print(count)
