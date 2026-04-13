"""
部分和問題のメモ化
(https://algo-method.com/tasks/438)
"""
import sys
sys.setrecursionlimit(10**6)

# 先頭から i 個の要素を使って、合計 j を作れるか？
# メモ化再帰
def func(i ,j) -> int:
  # 過去に計算済みの場合メモに記録された値を返す
  if memo[i][j] != -1: return memo[i][j]
  
  if i == 0:
    memo[i][j] = j == 0
  else:
    memo[i][j] = 0
    if j >= a[i - 1] and func(i - 1, j - a[i - 1]) == 1:
      memo[i][j] = 1
    if func(i - 1, j) == 1:
      memo[i][j] = 1
  return memo[i][j]

n,x = map(int, input().split())
a = list(map(int, input().split()))
# func(i, j) の値を記録するメモ(配列)を用意する
# -1 なら未記録、0 なら false、1 なら true
memo = [[-1] * (x + 1) for _ in range(n + 1)]
print("Yes" if func(n, x) == 1 else "No")

n,x = map(int, input().split())
a = list(map(int, input().split()))
dp = [False] * (x + 1)
dp[0] = True # 最初のマスは辿り着ける

# 動的計画法の解法
for i in range(n):
  for j in range(x, -1, -1):
    # j - a[i] を作れるなら → a[i] を足して j を作れる
    if j - a[i] >= 0 and dp[j - a[i]]:
      dp[j] = True
    if dp[x]:
      print("Yes")
      exit()
print("No")