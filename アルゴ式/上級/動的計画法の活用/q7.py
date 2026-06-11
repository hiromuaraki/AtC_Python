"""
ナップサック問題への導入
(https://algo-method.com/tasks/341)

最大価値

マスごとの最大価値
先頭から i 個見た時、
重さ j を作る時の最大価値

ナップサックでは、
「作れるか」ではなく
「その重さでの最大価値」
を状態として持つため、
遷移時に価値を加算して max で更新します。
"""

N,M = map(int, input().split())
A = list(map(int, input().split())) # 移動
B = list(map(int, input().split())) # 価値

dp = [[-1] * M for _ in range(N)]
dp[0][0] = 0 # マスを何も選ばない

for i in range(N):
    for j in range(M):
        if dp[i][j] < 0:
            continue
        # 選ばない（今までの価値を引き継ぐ）
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        
        if j + A[i] < M:
            # 選ぶ（今までの価値＋今回の価値）
            dp[i + 1][j + A[i]] = max(
                dp[i + 1][j + A[i]],
                dp[i][j] + B[i]
            )

print(dp[N - 1][M - 1])