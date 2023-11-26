import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append(input().rstrip())

a = list(set(a))   
a.sort()
a.sort(key = lambda x: len(x))

print(*a, sep = ' ')
