import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    cmd = input().split()    

    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stack) > 0:
            print(stack[len(stack) - 1])
            stack.pop()
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == "top":
        print(stack[len(stack) - 1] if len(stack) > 0 else -1)
    else:
        break
