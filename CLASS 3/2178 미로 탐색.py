import sys
from collections import deque
input = sys.stdin.readline

def BFS(row, col):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque()
    q.append((row, col))

    while q:
        row, col = q.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                q.append((nr, nc))
                maze[nr][nc] = maze[row][col] + 1
    return maze[N-1][M-1]

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

print(BFS(0,0))
