T = int(input())

dp = [1, 1]

for i in range(2, 31):
    value = dp[i - 1] + dp[i - 2] * 2
    dp.append(value)

for tc in range(1, T + 1):
    N = int(input())
    idx = N // 10

    print(f"#{tc} {dp[idx]}")
