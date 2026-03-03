"""
マスの移動 (1)
(https://algo-method.com/tasks/303)
"""

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n # マスを0から開始
for i in range(1, n):
  if i == 1:
    dp[i] = dp[i - 1] + a[i] # マスを一つ先へ移動
    continue
  dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + 2*a[i])
print(dp[n - 1])