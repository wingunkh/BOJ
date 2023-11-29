import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(result, plus, minus, multiply, divide, depth):
    global maximum
    global minimum
    
    if depth == n-1:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    
    if plus:
        dfs(result + a[depth+1], plus-1, minus, multiply, divide, depth+1)
    if minus:
        dfs(result - a[depth+1], plus, minus-1, multiply, divide, depth+1)
    if multiply:
        dfs(result * a[depth+1], plus, minus, multiply-1, divide, depth+1)
    if divide:
        dfs(int(result / a[depth+1]), plus, minus, multiply, divide-1, depth+1)

dfs(a[0], b[0], b[1], b[2], b[3], 0)

print(maximum)
print(minimum)
