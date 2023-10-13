import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
tmp = 0

for i in a:
    tmp += i
    s.append(tmp)
    
for _ in range(m):
    start, end = map(int, input().split())
    print(s[end] - s[start-1])
