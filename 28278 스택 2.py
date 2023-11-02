import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    data = list(map(int, input().split()))

    if data[0] == 1:
        a.append(data[1])
    elif data[0] == 2:
        if a:
            print(a.pop())
        else:
            print(-1)
    elif data[0] == 3:
        print(len(a))
    elif data[0] == 4:
        if a:
            print(0)
        else:
            print(1)
    else:
        if a:
            print(a[-1])
        else:
            print(-1)
