"""
コマの道順 (壁あり)
(https://algo-method.com/tasks/333)
"""

n = int(input())
s = [input() for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if s[i][j] == "#":
      continue
    if i - 1 >= 0:
      dp[i][j] += dp[i - 1][j]
    if j - 1 >= 0:
      dp[i][j] += dp[i][j - 1]
print(dp[n - 1][n - 1])