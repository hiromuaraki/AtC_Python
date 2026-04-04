"""
表と数値（２）
(https://algo-method.com/tasks/325)
"""

n = int(input())
dp = [[0] * n for _ in range(n)]
dp[0] = list(map(int, input().split()))

for i in range(1, n):
  for j in range(n):
    # 上のマスの遷移を集約
    dp[i][j] += dp[i - 1][j]
    # 左上のマスからの遷移を集約
    if j - 1 >= 0:
      dp[i][j] += dp[i - 1][j  -1]
    # 右上のマスからの遷移を集約
    if j + 1 < n:
      dp[i][j] += dp[i - 1][j + 1]
    dp[i][j] %= 100
print(dp[n - 1][n - 1])
