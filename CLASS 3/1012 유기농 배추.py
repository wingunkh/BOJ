import sys
sys.setrecursionlimit(10000)

def dfs(row, col):
    # 상, 하, 좌, 우로 인접한 배추 위치 확인
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 현재 위치 방문 처리
    field[row][col] = 0

    # 인접한 배추 위치 탐색
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        # 배추가 심어져 있는 위치이고 아직 방문하지 않았다면 DFS 호출
        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1:
            dfs(nr, nc)

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)] # M = 열의 길이, N = 행의 길이

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
