n, m = map(int, input().split())
a = list(map(int, input().split()))
max_sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= m and a[i] + a[j] + a[k] > max_sum:
                max_sum = a[i] + a[j] + a[k]

print(max_sum)
