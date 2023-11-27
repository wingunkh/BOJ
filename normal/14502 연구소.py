import sys, copy
from collections import deque
input = sys.stdin.readline

def dfs(depth):
    if depth == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                dfs(depth+1)
                a[i][j] = 0

def bfs():
    global result
    q = deque()
    tmp = copy.deepcopy(a)
    safe = 0

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for i in range(4):
            if 0 <= r + dr[i] < n and 0 <= c + dc[i] < m and tmp[r + dr[i]][c + dc[i]] == 0:
                tmp[r + dr[i]][c + dc[i]] = 2
                q.append((r + dr[i], c + dc[i]))
                
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                safe += 1

    result = max(result, safe)
                
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

dfs(0)

print(result)
