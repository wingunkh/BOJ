from collections import deque

n = int(input())
waiting = deque(list(map(int, input().split())))
stack = deque()
result = []
next = 1

while waiting:
    if waiting[0] == next:
        result.append(waiting.popleft())
        next += 1
    elif stack and stack[-1] == next:
        result.append(stack.pop())
        next += 1
    else:
        stack.append(waiting.popleft())
            
while stack:
    result.append(stack.pop())

if result == sorted(result):
    print("Nice")
else:
    print("Sad")
