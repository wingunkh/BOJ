import sys
input = sys.stdin.readline

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())

if n == 0:
    print(0)
else:
    array = [int(input()) for _ in range(n)]
    array.sort()

    tm = round(n * 0.15)
    if tm != 0
        array = array[tm:-tm]

    print(round(sum(array) / (n - 2*tm)))
