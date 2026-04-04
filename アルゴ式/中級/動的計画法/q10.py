"""
3つの仕事
状態定義の勉強になった。
(https://algo-method.com/tasks/41)

同じ仕事は連続して選べない
＝今日j選ぶなら昨日はj以外

遷移式
dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i][0]
今の状態 = 過去の状態 + 今の選択
"""

n = int(input())
dp = [[0] * 3 for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]

# 何でも選べる（まだ何も制約を受けていない状態）
for i in range(3):
  dp[0][i] = a[0][i]

for i in range(1, n):
  # 連続した仕事は選べない
  # i日目に仕事jした時の最大報酬
  dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a[i][0]
  dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + a[i][1]
  dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + a[i][2]
print(max(dp[n - 1]))