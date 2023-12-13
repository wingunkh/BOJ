n, m = map(int, input().split())
r, c, i = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = 0

while True:
    if a[r][c] != -1:
        a[r][c] = -1
        result += 1

    count = 0

    while count < 4:
        count += 1
        i = (i-1) % 4

        if 1 <= r + dr[i] < n-1 and 1 <= c + dc[i] < m-1 and a[r + dr[i]][c + dc[i]] == 0:
            r, c = r + dr[i], c + dc[i]
            break
    else:
        if a[r - dr[i]][c - dc[i]] == 1:
            break
        else:
            r, c = r - dr[i], c - dc[i]
        
print(result)
