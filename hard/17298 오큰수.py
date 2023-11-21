import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
answer= [-1 for _ in range(n)]

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        idx = stack.pop()
        answer[idx] = a[i]
    stack.append(i)

print(*answer, sep = ' ')
