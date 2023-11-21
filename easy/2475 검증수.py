a = list(map(int, input().split()))
result = 0

for i in a:
    result += i ** 2

print(result % 10)
