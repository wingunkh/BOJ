def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = []
b = []
result = 0

for _ in range(n):
    a.append(int(input()))

for i in range(1, n):
    b.append(a[i] - a[i-1])

GCD = gcd(b[0], b[1])

for i in range(2, len(b)):
    GCD = gcd(GCD, b[i])

for i in b:
    if i > GCD:
        result += i // GCD - 1

print(result)
