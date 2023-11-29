import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
target = [list(map(int, input().split())) for _ in range(m)]
a = [[0 for _ in range(n+1)] for i in range(n+1)]
s = [[0 for _ in range(n+1)] for i in range(n+1)]

for i in range(n):
    for j in range(n):
        a[i+1][j+1] = tmp[i][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = a[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]

for x1, y1, x2, y2 in target:
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])
