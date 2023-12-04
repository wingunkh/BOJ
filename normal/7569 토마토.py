import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()

    for k in range(h):
        for i in range(m):
            for j in range(n):
                if a[k][i][j] == 1:
                    q.append((k, i, j))

    while q:
        d, r, c = q.popleft()

        for i in range(6):
            nd, nr, nc = d + dd[i], r + dr[i], c + dc[i]
            if 0 <= nd < h and 0 <= nr < m and 0 <= nc < n and a[nd][nr][nc] == 0:
                a[nd][nr][nc] = a[d][r][c] + 1
                q.append((nd, nr, nc))
                
n, m, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dd = [0, 0, 0, 0, -1, 1]
result = 0

bfs()

for k in range(h):
    for i in range(m):
        for j in range(n):
            if a[k][i][j] == 0:
                print(-1)
                exit()
            else:
                result = max(result, a[k][i][j])
else:
    print(result-1)
