n = int(input())
a = []
stack = []
answer = []
next = 1

for _ in range(n):
    a.append(int(input()))

for i in a:
    while next <= i:
        stack.append(next)
        answer.append('+')
        next += 1
        
    data = stack.pop()
    if data == i:
        answer.append('-')
    else:
        print("NO")
        break
else:
    print(*answer, sep = '\n')
