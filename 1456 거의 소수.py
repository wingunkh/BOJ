n, m = map(int, input().split())
a = [i for i in range(int(m ** 0.5)+1)]
a[0] = 0
a[1] = 0
result = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    
    for j in range(i+i, len(a), i):
        a[j] = 0

for i in a:
    if a[i] == 0:
        continue
    
    tmp = i
    
    while tmp <= m:
        tmp *= i
        if n <= tmp <= m:
            result += 1

print(result)
