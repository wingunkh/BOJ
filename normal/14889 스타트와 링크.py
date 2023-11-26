import sys
input = sys.stdin.readline

def dfs(index, depth):
    global result
    
    if depth == n // 2:
        start = 0
        link = 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += a[i][j]
                elif not visited[i] and not visited[j]:
                    link += a[i][j]

        result = min(result, abs(start - link))
        return
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, depth+1)
            visited[i] = False

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = sys.maxsize

dfs(0, 0)

print(result)
