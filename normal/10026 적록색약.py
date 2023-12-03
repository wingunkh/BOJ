from collections import deque

def bfs(r, c, color):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if 0 <= next_r < n and 0 <= next_c < n and a[next_r][next_c] == color and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True

n = int(input())
a = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result1 = 0
result2 = 0

for _ in range(n):
    a.append(list(input()))

visited = [[False for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(r, c, a[r][c])
            result1 += 1

for r in range(n):
    for c in range(n):
        if a[r][c] == 'R':
            a[r][c] = 'G'

visited = [[False for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(r, c, a[r][c])
            result2 += 1

print(result1, result2)
