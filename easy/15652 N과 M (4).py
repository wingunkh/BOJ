def dfs(index, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(index, n+1):
        result.append(i)
        dfs(i, depth+1)
        result.pop()

n, m = map(int, input().split())
result = []

dfs(1, 0)
