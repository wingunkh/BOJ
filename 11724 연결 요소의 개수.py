import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
a = [[] for _ in range(n+1)] 
visited = [False for _ in range(n+1)]
count = 0

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
