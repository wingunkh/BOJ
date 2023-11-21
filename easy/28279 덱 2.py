import sys
from collections import deque
input = sys.stdin.readline

d = deque()
n = int(input())

for _ in range(n):
    operation = list(input().split())

    if operation[0] == '1':
        d.appendleft(operation[1])
    elif operation[0] == '2':
        d.append(operation[1])
    elif operation[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif operation[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif operation[0] == '5':
        print(len(d))
    elif operation[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif operation[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)
