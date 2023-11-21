n, k = map(int, input().split())
a = []
result = 0

for _ in range(n):
    a.append(int(input()))

a.sort(reverse = True)

for i in a:
    if k >= i:
        result += k // i
        k %= i
        
print(result)
