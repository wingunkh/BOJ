import sys
input= sys.stdin.readline

n, m = map(int, input().split())
a = [[0 for _ in range(n+1)]]
s = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n):
    a.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = a[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]
    
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    print(s[r2][c2] - s[r1-1][c2] - s[r2][c1-1] + s[r1-1][c1-1])
