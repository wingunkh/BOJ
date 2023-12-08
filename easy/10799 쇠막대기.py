s = list(input())
stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        if s[i-1] == '(':
            stack.pop()
            result += stack.count('(')
        else:
            result += 1
            stack.pop()

print(result)
