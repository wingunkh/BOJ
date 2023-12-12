from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        now_r, now_c, depth = q.popleft()

        if now_r == end_r and now_c == end_c:
            print(depth)
            break

        for i in range(8):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c]:
                q.append((next_r, next_c, depth+1))
                visited[next_r][next_c] = True

t = int(input())
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    n = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]

    bfs(start_r, start_c)
