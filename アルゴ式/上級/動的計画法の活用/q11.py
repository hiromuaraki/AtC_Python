"""
もう一つのナップサック問題
(https://algo-method.com/tasks/7147e09c64ad8783)

2次元
合計 j の重さを作るための最大価値

1次元
価値 v を作る最小の重さ

"""

N,M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

# dp = [[-1] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     for j in range(M + 1):
#         if dp[i][j] == -1:
#             continue
#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = max(
#                 dp[i + 1][j + W[i]],
#                 dp[i][j] + V[i]
#             )
# print(dp[M])

INF = 10**18
MAX_V = sum(V)
# dp[v]
# 価値 v を作るための最小重さ
dp = [INF] * (MAX_V + 1)

dp[0] = 0
for i in range(N):
    for v in range(MAX_V, -1, -1):
        if dp[v] == INF:
            continue
        nv = v + V[i]
    
        dp[nv] = min(
            dp[nv],
            dp[v] + W[i]
        )

# 重さM以内で作れる最大価値
ans = 0
for v in range(MAX_V + 1):
    if dp[v] <= M:
        ans = max(ans, v)
print(ans)
