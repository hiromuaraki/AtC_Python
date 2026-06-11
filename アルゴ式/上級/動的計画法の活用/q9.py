"""
マス目の経路最適化
(https://algo-method.com/tasks/856)

P[行][列]
dp[列][最後の行]
列を進みながら現在行→次の行へ遷移を全探索
"""

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [A, B, C]
INF = 10**18

# dp[i][r]
# i列目まで見た時、
# i列目で r 行目を選んだ時の最小コスト
dp = [[INF] * 3 for _ in range(N)]

# 0列目初期化
for r in range(3):
    dp[0][r] = 0

# 列を進める
for i in range(N - 1):
    # 現在いる行
    for now in range(3):
        # 次に行く行
        for next in range(3):
            cost = abs(P[now][i] - P[next][i + 1])
            
            dp[i + 1][next] = min(
                dp[i + 1][next],
                dp[i][now] + cost
            )
print(min(dp[N - 1]))
