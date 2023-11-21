import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)] # 그래프를 인접 행렬로 구현

for i in range(1, n+1):
    a[i][i] = 0

for i in range(m):
    s, e, w = map(int, input().split())
    if a[s][e] > w:
        a[s][e] = w

for k in range(1, n+1): # 경유지
    for s in range(1, n+1): # 출발지
        for e in range(1, n+1): # 도착지
            a[s][e] = min(a[s][e], a[s][k] + a[k][e])

for s in range(1, n+1):
    for e in range(1, n+1):
        if a[s][e] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(a[s][e], end = ' ')
    print()
