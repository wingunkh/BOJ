from collections import deque

n = int(input())
a = [i for i in range(1, n+1)]
b = list(map(int, input().split()))
q = deque()
result = []

for i in range(n):
    q.append((a[i], b[i]))

while q:
    number, paper = q.popleft()
    result.append(number)

    if paper > 0:
        q.rotate(-(paper-1))
        # 원형 큐를 시계 반대 방향으로 회전
        # q.popleft() -> 시계 반대 방향으로 한 칸 회전한 것과 같으므로 한 칸 덜 회전해야 한다.
    else:
        q.rotate(-paper)
        # 원형 큐를 시계 방향으로 회전

print(*result, sep = ' ')
