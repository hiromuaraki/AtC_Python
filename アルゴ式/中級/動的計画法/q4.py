"""
すごろく
(https://algo-method.com/tasks/323)

部分和問題
マスNに到達できるか？

dp[i - d[j]] がやっていること
その一歩手前に立てるかどうかの確認

マスが存在するか確認
その一歩手前に辿り着けるか確認
辿り着けるなら今も辿り着ける
"""

n, m = map(int, input().split())
d = list(map(int, input().split()))
dp = [False] * (n + 1) # マスiに辿り着けるかを管理する配列
dp[0] = True # マス0には辿り着ける

for i in range(1, n + 1):
  for j in range(m):
    # マスの存在チェック＋マスi - d[j]に辿り着けているか？
    if i - d[j] >= 0 and dp[i - d[j]]:
      dp[i] = True
      break
print("Yes" if dp[n] else "No")