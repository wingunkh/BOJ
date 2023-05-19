import sys
from collections import deque
input = sys.stdin.readline

def DFS(start: int) -> None:
    visited[start] = True
    print(start, end = ' ')

    # 인접 정점들에 대해 반복
    for i in range(1, N + 1):
        # 방문하지 않았고, 간선이 존재하는 경우
        if not visited[i] and graph[start][i]:
            DFS(i)

def BFS(start: int) -> None:
    # 덱을 이용한 큐 생성
    q = deque()
    
    q.append(start)
    visited[start] = True
    print(start, end = ' ')

    while q:
        start = q.popleft()
        
        for i in range(1, N + 1):
            if not visited[i] and graph[start][i]:
                q.append(i)
                visited[i] = True
                print(i, end = ' ')

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

DFS(V)

print()
visited = [False] * (N + 1)

BFS(V)
