import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    a[r][c] = 0

    while q:
        r, c = q.popleft()

        for i in range(8):
            next_r, next_c = r + dr[i], c + dc[i]
            if 0 <= next_r < m and 0 <= next_c < n and a[next_r][next_c] == 1:
                q.append((next_r, next_c))
                a[next_r][next_c] = 0
                
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = [list(map(int, input().split())) for _ in range(m)]
    result = 0

    for r in range(m):
        for c in range(n):
            if a[r][c] == 1:
                result += 1
                bfs(r, c)

    print(result)
