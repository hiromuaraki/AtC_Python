"""
部分和問題 (最小個数)
(https://algo-method.com/tasks/350)
最小個数を持つ
"""

N,M = map(int, input().split())
W = list(map(int, input().split()))
INF = 10**8
# dp[N][M] = i個見た時合計jを何個作れるかを管理する配列（最小個数）
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == INF:
            continue
        # 選ばない（合計変化なし）
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        
        # 選ぶ（合計変化あり）
        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = min(dp[i + 1][j + W[i]], dp[i][j] + 1)

print(dp[N][M] if dp[N][M] != INF else -1)