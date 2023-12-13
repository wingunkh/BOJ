t = int(input())
a = [[0 for _ in range(30)] for _ in range(30)]

for i in range(1, 30):
    a[i][0] = 1
    a[i][1] = i
    a[i][i] = 1

for i in range(2, 30):
    for j in range(2, i):
        a[i][j] = a[i-1][j] + a[i-1][j-1]

for _ in range(t):
    n, m = map(int, input().split())

    print(a[m][n])
