n = int(input())
a = list(map(int, input().split()))
s = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if a[j+1] > a[j]:
            break
        else:
            a[j+1], a[j] = a[j], a[j+1]

s[0] = a[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]

print(sum(s))
