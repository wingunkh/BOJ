import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input().split()    

    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        print(stack.pop(-1) if stack else -1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == "top":
        print(stack[-1] if stack else -1)
    else:
        break
