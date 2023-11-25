def dfs(x, sum):
    global result

    if x == n:
        return

    sum += a[x]

    if sum == m:
        result += 1

    dfs(x+1, sum)
    dfs(x+1, sum - a[x])

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0

dfs(0, 0)

print(result)
