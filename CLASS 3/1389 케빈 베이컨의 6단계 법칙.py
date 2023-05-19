import sys
from collections import deque
input = sys.stdin.readline

def BFS(start: int) -> int:
    visited = [False] * (N + 1)
    score = [0] * (N + 1)
    q = deque()
    
    q.append(start)
    visited[start] = True

    while q:
        a = q.popleft()
        
        for i in range(1, N + 1):
            if not visited[i] and graph[a][i]:
                q.append(i)
                visited[i] = True
                score[i] = score[a] + 1

    return sum(score)
                
N, M = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

for i in range(1, N + 1):
    result.append(BFS(i))

print(result.index(min(result)) + 1)
