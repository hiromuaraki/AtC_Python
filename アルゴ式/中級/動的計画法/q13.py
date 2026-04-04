"""
コマの道順 (重み付き)
(https://algo-method.com/tasks/334)

dp[i][j] = max(上からのマスの集約＋左からのマスの集約) + 現在のマス
= マス(i, j)へ移動する最大のコスト

どこからくるか：上からのマス＋左からのマス
比較する対象：上からの移動コスト、左からの移動コスト
最後に何を足すか：現在いるマスの数
"""

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = a[0][0]

for i in range(n):
  for j in range(n):
    if i == 0 and j == 0:
      continue
    val = -10 ** 18
    # 上から来るマスを集約して足す
    if i - 1 >= 0:
      val = max(val, dp[i - 1][j])
    # 左から来るマスを集約して足す
    if j - 1 >= 0:
      val = max(val, dp[i][j - 1])
    dp[i][j] += val + a[i][j]
print(dp[n - 1][n - 1])