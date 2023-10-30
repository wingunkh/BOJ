import sys
input = sys.stdin.readline

t = int(input())
a = [i for i in range(1000001)]
a[1] = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    else:
        for j in range(i+i, len(a), i):
            a[j] = 0

for _ in range(t):
    n = int(input())
    result = 0
    
    for j in range(2, n // 2 + 1):
        if a[j] and a[n-j]:
            result += 1

    print(result)
