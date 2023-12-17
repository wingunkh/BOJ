n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
# dp[a] = 0번째 원소부터 a번째 원소까지의 최대 연속합
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))
