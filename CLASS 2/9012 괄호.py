n = int(input())

for _ in range(n):
    stack = []
    string = input()

    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
