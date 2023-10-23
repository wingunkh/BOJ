from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r,c))

    while q:
        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < n and 0 <= next_col < m and a[next_row][next_col] == 1:
                a[next_row][next_col] = a[now_row][now_col] + 1
                q.append((next_row, next_col))
            
n, m = map(int, input().split())
a = []
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for _ in range(n):
    a.append(list(map(int, input())))

bfs(0, 0)

print(a[n-1][m-1])
