"""
部分和問題 (K 個以内)
(https://algo-method.com/tasks/312)

現在の合計
現在の個数

dp[i][j][k]
= 先頭から i 個見た時 k 個使って合計 j を作れる

dp[j][k]
= 合計 j を作るための個数

dp[j] = 合計jを作るための最小個数
"""

N,M,K = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**9

# dp[j]
# 合計 j を
# k個使って作れるか
dp = [INF] * (M + 1)

dp[0] = 0

for a_i in A:
    # 同じ数字を複数回使わないため逆順方向
    for j in range(M, -1, -1):
        
        if dp[j] == INF:
            continue

        # aを選ぶ
        if j + a_i <= M:
            dp[j + a_i] = min(
                dp[j + a_i],
                dp[j] + 1
            )
# M を K 個以内で作れるか
print("Yes" if dp[M] <= K else "No")



