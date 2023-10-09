from collections import deque

def BFS(r, c):
    count = 1
    q = deque()
    q.append((r,c))
    
    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc]:
                count += 1
                graph[nr][nc] = 0
                q.append((nr, nc))
    return count
                
n = int(input())
graph = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
answer = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
         if graph[i][j]:
             graph[i][j] = 0
             answer.append(BFS(i, j))

print(len(answer))
answer.sort()

for i in answer:
    print(i)
