def dynamic(n: int) -> int:
    # 수를 1로 만들기 위해 필요한 연산의 최소 횟수를 저장
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # 현재 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

X = int(input())
print(dynamic(X))
