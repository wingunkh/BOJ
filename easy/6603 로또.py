def dfs(index, depth):
    if depth == 6:
        for i in range(len(a)):
            if visited[i]:
                print(a[i], end = ' ')
        print()
        return
    
    for i in range(index, len(a)):
        visited[i] = True
        dfs(i+1, depth+1)
        visited[i] = False
        
while True:
    buff = list(map(int, input().split()))
    k = buff[0]
    a = buff[1:]
    visited = [False for _ in range(len(a))]

    if k == 0:
        break

    dfs(0, 0)
    print()
