import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v, end = ' ')

    for i in a[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    print(v, end = ' ')

    while q:
        now = q.popleft()
        
        for i in a[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                print(i, end = ' ')
 
n, m, v = map(int, input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in a:
    i.sort()

visited = [False for _ in range(n+1)]
dfs(v)

print()

visited = [False for _ in range(n+1)]
bfs(v)
