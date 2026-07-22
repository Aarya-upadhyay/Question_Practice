"""def push(stack,top):
    if top!=N:
        stack.append(input())
        top+=1
def pop(stack,top):
    if top!=-1:
        stack.remove(stack[top])
        top-=1
def peek(stack):
    return stack[-1]
N=int(input())
stack=[]
top=-1
for _ in range(N):
    push(stack,top)
M=int(input())
for _ in range(M):
    pop(stack,top)
if stack:
    print("FALSE")
else:
    print("TRUE")
p=peek(stack)
print(p)
print(len(stack))"""

# in above logic it is fine but the only thing which would not work is the updation of top now i get it why it wont
stack=[]
n=int(input())
for _ in range(n):
    stack.append(input())
m=int(input())
for _ in range(m):
    if stack:
        stack.pop()
if stack:
    print("FALSE")
else:
    print("TRUE")
print(stack[-1])
print(len(stack))
