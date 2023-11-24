import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()

    for i in range(m):
        for j in range(n):
            if a[i][j] == 1:
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < m and 0 <= nc < n and a[nr][nc] == 0:
                a[nr][nc] = a[r][c] + 1
                q.append((nr, nc))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

bfs()

for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            print(-1)
            exit()
        else:
            result = max(result, a[i][j])
else:
    print(result-1)
