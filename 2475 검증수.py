a = list(map(int, input().split()))
result = 0
mod = 10

for i in a:
    result += i ** 2

print(result % mod)
