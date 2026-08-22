import heapq

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

m = len(arr[0])

res = [[float('inf')] * m for _ in range(n)]

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

res[0][0] = 0

heap = []
heapq.heappush(heap, (0, (0, 0)))


def valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def dji(arr, heap, res):

    while heap:

        d, pair = heapq.heappop(heap)

        r, c = pair

        if d > res[r][c]:
            continue

        for k in range(4):

            ro = r + x[k]
            co = c + y[k]

            if not valid(ro, co, n, m):
                continue

            abs_dif = abs(arr[r][c] - arr[ro][co])

            new = max(d, abs_dif)

            if new < res[ro][co]:

                res[ro][co] = new

                heapq.heappush(heap, (new, (ro, co)))

    return res[n-1][m-1]


print(dji(arr, heap, res))