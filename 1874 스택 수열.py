n = int(input())
stack = []
result = []
next = 1

for i in range(n):
    target = int(input())

    while next <= target:
        stack.append(next)
        result.append('+')
        next += 1

    data = stack.pop()
    result.append('-')

    if data != target:
        print("NO")
        break
else:
    print(*result, sep = "\n")
