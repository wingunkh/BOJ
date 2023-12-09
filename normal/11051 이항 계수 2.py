n, m = map(int, input().split())
dp = [[i for i in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i
    dp[i][i] = 1

for i in range(n+1):
    for j in range(2, i):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007
        # 모듈러 연산의 특성 : (A + B) % N = (A % N + B % N) % N

print(dp[n][m])
