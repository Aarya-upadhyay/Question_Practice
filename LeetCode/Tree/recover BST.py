n = int(input())
arr = input().split()

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if arr[0] != "null":
    root = Node(int(arr[0]))
else:
    root = None

from collections import deque

q = deque([root])
i = 1

while i < n and q:
    c = q.popleft()

    if i < n:
        if arr[i] != "null":
            c.left = Node(int(arr[i]))
            q.append(c.left)
        i += 1

    if i < n:
        if arr[i] != "null":
            c.right = Node(int(arr[i]))
            q.append(c.right)
        i += 1


def findreorder(root):

    prev = None
    g = 0

    g1f = None
    g1s = None
    g2f = None
    g2s = None

    def inorder(r):
        nonlocal prev, g, g1f, g1s, g2f, g2s

        if r is None:
            return

        inorder(r.left)

        if prev is not None and r.val < prev.val:

            if g == 0:
                g1f = prev
                g1s = r
                g += 1

            else:
                g2f = prev
                g2s = r
                g += 1

        prev = r

        inorder(r.right)

    inorder(root)

    # One inversion
    if g == 1:
        g1f.val, g1s.val = g1s.val, g1f.val

    # Two inversions
    else:
        g1f.val, g2s.val = g2s.val, g1f.val


findreorder(root)


def print_inorder(r):
    if r is None:
        return

    print_inorder(r.left)
    print(r.val, end=" ")
    print_inorder(r.right)


print_inorder(root)