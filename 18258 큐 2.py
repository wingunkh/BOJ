import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())

for _ in range(n):
    operation = list(input().split())

    if operation[0] == "push":
        q.append(operation[1])
    elif operation[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif operation[0] == "size":
        print(len(q))
    elif operation[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif operation[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
