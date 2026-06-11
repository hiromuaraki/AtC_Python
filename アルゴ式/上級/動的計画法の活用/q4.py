"""
部分和問題 (数え上げ)
(https://algo-method.com/tasks/310)
通り数を持つ
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
MOD = 1000

# i個見た時合計jを作る方法の通り数を持たせる
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1 # 何も選ばず0を作る方法は1通り（何も選ばない）

for i in range(N):
    for j in range(M + 1):
        if not dp[i][j]:
            continue
        # 今までの方法数を引き継ぐ
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        
        if j + A[i] <= M:
            dp[i + 1][j + A[i]] += dp[i][j]
            dp[i + 1][j + A[i]] %= MOD

print(dp[N][M])