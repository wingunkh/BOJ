def dfs(x, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(x+1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i, depth+1)
            visited[i] = False
            result.pop()

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
result = []

dfs(0, 0)
