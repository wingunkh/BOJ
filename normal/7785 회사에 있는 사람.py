import sys
input = sys.stdin.readline

n = int(input())
dic = dict()

for _ in range(n):
    a, b = input().split()

    if b == "enter":
        dic[a] = b
    else:
        del dic[a]

result = sorted(dic.keys(), reverse = True)

print(*result, sep = "\n")
