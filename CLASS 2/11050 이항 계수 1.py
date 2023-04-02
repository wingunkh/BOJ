from math import factorial
n, k = map(int, input().split())
res = factorial(n) // (factorial(k) * factorial(n-k))
print(res)
