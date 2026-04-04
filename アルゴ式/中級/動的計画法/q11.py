"""
コマの道順
(https://algo-method.com/tasks/329)

DPはどこからきたかを考える
最後の移動で場合分け
・上からくる：(i - 1, j)
・左からくる：(i, j - 1)
dp[i][j] = マス（i, j)に到達する方法の数
dp[i][j] = 上から来る通り数＋左から来る通り数
"""

n = int(input())
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 # 左上のマスにコマを一つおく
for i in range(n):
  for j in range(n):
    # 上のマスを集約し足す
    if i - 1 >= 0:
      dp[i][j] += dp[i - 1][j]
    # 左のマスを集約し足す
    if j - 1 >= 0:
      dp[i][j] += dp[i][j - 1]
print(dp[n - 1][n - 1])