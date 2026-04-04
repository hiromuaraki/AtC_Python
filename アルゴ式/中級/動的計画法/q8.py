"""
表と数値 (1)
(https://algo-method.com/tasks/324)

左上・・・(i - 1, j - 1)
真上・・・(i - 1, j)
右上・・・(i - 1, j + 1)
"""

a = list(map(int, input().split()))
n = 4
dp = [[0] * n for _ in range(n)]
dp[0] = a
for i in range(1, n):
  for j in range(n):
    # 真上の場合
    dp[i][j] += dp[i - 1][j]
    # 左上の場合
    if j - 1 >= 0:
      dp[i][j] += dp[i - 1][j - 1]
    # 右上の場合
    if j + 1 < n:
      dp[i][j] += dp[i - 1][j + 1]
print(dp[n - 1][n - 1])