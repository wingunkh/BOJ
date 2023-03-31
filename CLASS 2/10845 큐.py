import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(-1 if not queue else queue.pop(0))
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(-1 if not queue else queue[0])
    elif cmd[0] == "back":
        print(-1 if not queue else queue[-1])
    else:
        break
