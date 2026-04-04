"""
マス目上の最短経路の本数
（https://algo-method.com/descriptions/78）

直前の行動で場合分け
マス(0, 0)からマス(i, j)へと至る経路の本数

・上のマスから下のマス＝(i - 1, j)
・左のマスから右のマス＝(i, j - 1)
＝dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
＝最短経路の本数
"""

n = int(input())
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1 # (0, 0)の開始 必ず1通り存在する（初期値）
for i in range(n):
  for j in range(n):
    # 上から来る場合
    if i - 1 >= 0:
      dp[i][j] += dp[i - 1][j]
    # 左から来る場合
    if j - 1 >= 0:
      dp[i][j] += dp[i][j - 1]
print(dp[n - 1][n - 1])