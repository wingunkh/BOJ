m = int(input())
a = list(map(int, input().split()))
k = int(input())
result = 0

for i in a:
    buff = 1
    for j in range(k):
        buff *= ((i-j) / (sum(a) - j))
    result += buff

print(result)
