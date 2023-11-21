import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(*a, sep = "\n")
