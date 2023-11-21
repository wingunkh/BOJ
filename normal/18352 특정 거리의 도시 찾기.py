import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]
found = False

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
                result[i] = result[now] + 1 # 최단 거리 갱신

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

bfs(x)

for i in range(1, n+1):
    if result[i] == k:
        found = True
        break

if found:
   for i in range(1, n+1):
       if result[i] == k:
           print(i)
else:
    print(-1)
