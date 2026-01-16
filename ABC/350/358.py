"""
B問題_Ticket Counter
(https://atcoder.jp/contests/abc358/tasks/abc358_b)
シミュレーション問題

前の人が購入中かどうかをどう定義するか？

必要な変数
・前回チケット購入し終えた時間
・購入手続き中かどうか
その判断は、で前回の購入し終えた時間以下か以上かで判断
購入時間 <= time：購入手続き開始
購入時間 > time：購入手続き中

proc_time = max(proc_time, time) + a

"""

n,a = map(int, input().split())
t = list(map(int, input().split()))

proc_time = 0
for i in range(n):
  time = t[i]
  # 購入手続き中か
  if proc_time <= time:
    proc_time = time + a
  else:
    proc_time = proc_time + a
  print(proc_time)