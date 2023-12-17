n = int(input())
buff = list(map(int, input().split()))
visited = [False for _ in range(n+1)]
stack = []
result = []

def dfs(index, depth):
    if depth == n:
        result.append(stack[0:4])
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs(i, depth+1)
            visited[i] = False
            stack.pop()
        
dfs(0, 0)

if buff[0] == 1:
    print(*result[buff[1] - 1])
else:
    print(result.index(buff[1:5]) + 1)
