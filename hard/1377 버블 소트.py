import sys
input = sys.stdin.readline

n = int(input())
a = []
s = []
max = 0

for i in range(n):
    a.append((int(input()), i))

s = sorted(a)

for i in range(n):
    if s[i][1] - a[i][1] > max:
        max = s[i][1] - a[i][1]

print(max+1)
