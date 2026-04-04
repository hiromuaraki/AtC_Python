"""
コマの道順 (右上から)
(https://algo-method.com/tasks/335)
"""

INF = 10**18
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * n for _ in range(n)]
dp[0][n - 1] = a[0][n - 1]

for i in range(n):
  for j in range(n - 1, -1, -1):
    # 上から来るマスを集約
    if i - 1 >= 0:
      dp[i][j] = min(dp[i][j], dp[i - 1][j] + a[i][j])
    # 右から来るマスを集約
    if j + 1 < n:
      dp[i][j] = min(dp[i][j], dp[i][j + 1] + a[i][j])
print(dp[n - 1][0])