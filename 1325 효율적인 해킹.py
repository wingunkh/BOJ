import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        
        for i in a[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result[v] += 1

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
maximum = 0

for _ in range(m):
    e, s = map(int, input().split())
    a[s].append(e)

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    bfs(i)

maximum = max(result)

for i in range(1, n+1):
    if result[i] == maximum:
        print(i, end = ' ')
