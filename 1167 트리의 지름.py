import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, w):
    visited[v] = True

    for node, weight in a[v]:
        if not visited[node]:
            dfs(node, w + weight)

    result[v] = w

n = int(input())
a = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for i in range(n):
    buff = list(map(int, input().split()))
    node = buff[0]
    buff = buff[1:-1]

    for j in range(0, len(buff), 2):
        a[node].append((buff[j], buff[j+1]))


dfs(1, 0)
farthest_node = result.index(max(result))

visited = [False for _ in range(n+1)]
dfs(farthest_node, 0)

print(max(result))
