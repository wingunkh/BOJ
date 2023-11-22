import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [(0, 0)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# dp[i][j] = 최대 무게가 j인 가방에서 i번째 물건까지 판단했을 때의 최대 가치

for _ in range(n):
    w, v = map(int, input().split())
    a.append((w, v))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = a[i][0]
        value = a[i][1]

        if j < weight: # 가방에 물건을 넣을 수 없을 때
            dp[i][j] = dp[i-1][j]
        else: # 가방에 물건을 넣을 수 있을 때
            dp[i][j] = max(dp[i-1][j - weight] + value, dp[i-1][j])

print(dp[n][k])
