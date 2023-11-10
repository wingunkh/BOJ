import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
minimum = sys.maxsize
result = 0

for i in range(1, n+1):
    a[i][i] = 0

for _ in range(m):
    s, e = map(int, input().split())
    a[s][e] = 1
    a[e][s] = 1

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if a[s][k] != sys.maxsize and a[k][e] != sys.maxsize:
                a[s][e] = min(a[s][e], a[s][k] + a[k][e])

for s in range(1, n+1):
    sum = 0

    for e in range(1, n+1):
        sum += a[s][e]

    if sum < minimum:
        minimum = sum
        result = s

print(result)
