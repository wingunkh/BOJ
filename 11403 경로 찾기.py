n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for k in range(n):
    for s in range(n):
        for e in range(n):
            if a[s][k] == 1 and a[k][e] == 1:
                a[s][e] = 1

for s in range(n):
    for e in range(n):
        print(a[s][e], end = ' ')
    print()
