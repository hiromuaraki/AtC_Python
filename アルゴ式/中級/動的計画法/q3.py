"""
マスの移動 (2)
(https://algo-method.com/tasks/306)

M通りの行動をとる
"""

n,M = map(int, input().split())
a = list(map(int, input().split()))
INF = 10**6 # 最小コストの初期値＝あり得ない値を設定
dp = [INF] * n
dp[0] = 0 # 初期値を設定（マスは０開始）
for i in range(1, n):
  for m in range(1, M + 1): # M+1(M以上）
    # マスが存在するか（負の場合は存在しない）  
    # i - j >= 0ならマスが存在する
    if i - m < 0: continue
    dp[i] = min(dp[i], dp[i - m] + a[i]*m)
print(dp[n - 1])