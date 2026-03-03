"""
階段ののぼり方
(https://algo-method.com/tasks/304)

N弾の階段 2通り の方法で階段を登る

最後の行動で場合分け
・１つ前の階段から登る
・２つ前の階段から登る
dp(n) = dp(n - 1) + dp(n - 2)
"""

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1 # 0段目に行く方法は1通り
dp[1] = 1 # 1段目に行く方法は1通り

for i in range(2, n + 1):
  # 最後の行動で場合分け
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])