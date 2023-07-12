import sys
input = sys.stdin.readline

def DFS(start):
    visited[start] = True
    
    for i in range(1, node + 1):
        if not visited[i] and graph[start][i]:
            DFS(i)

node = int(input())
edge = int(input())
graph = [[False] * (node + 1) for _ in range(node + 1)]
visited = [False] * (node + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

DFS(1)

print(visited.count(True) - 1)
