"""
ナップサック問題
(https://algo-method.com/tasks/342)

最大価値

先頭から i 個見た時、合計 j の重さを作れる最大価値
"""
N,M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
dp = [[-1] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    for j in range(M + 1):
        if dp[i][j] < 0:
            continue
        # 選ばない
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        
        # 選ぶ
        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = max(
                dp[i + 1][j + W[i]], # 重さ j の価値
                dp[i][j] + V[i] # 現在の価値＋今回の価値
            )
print(max(dp[N]))


