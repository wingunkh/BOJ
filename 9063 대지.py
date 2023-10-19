import sys
input = sys.stdin.readline

n = int(input())
x_list = []
y_list = []

for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))
