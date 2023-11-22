n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]
# dp[i] = a[i]를 마지막 값으로 가지는 가장 긴 LIS의 길이

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
