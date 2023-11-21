from collections import deque

def pour(x, y):
    if not visited[x][y]:
        q.append((x, y))
        visited[x][y] = True

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            result.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        pour(x - water, y)
        # y -> x
        water = min(y, a-x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        pour(x, y - water)
        # z -> x
        water = min(z, a-x)
        pour(x + water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y + water)

a, b, c = map(int, input().split())
q = deque()
visited = [[False for _ in range(b+1)] for _ in range(a+1)]
q.append((0, 0))
visited[0][0] = True
result = []

bfs()

result.sort()
print(*result, sep = ' ')
