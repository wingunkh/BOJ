import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
sec = sys.maxsize
floor = 0

for f in range(257):
    to_delete, to_create = 0, 0

    for i in range(n):
        for j in range(m):
            if array[i][j] >= f:
                to_delete += array[i][j] - f
            else:
                to_create += f - array[i][j]

    if b >= to_create - to_delete:
        if to_create + (to_delete * 2) <= sec:
            sec = to_create + (to_delete * 2)
            floor = f

print(sec, floor)
