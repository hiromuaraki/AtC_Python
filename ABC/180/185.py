"""
B問題_Smartphone Addiction
難しい
(https://atcoder.jp/contests/abc185/tasks/abc185_b)

必要な変数
pre：前回イベントの時刻
battery：現在の量
"""

n,m,t = map(int, input().split())
pre = 0
battery = n
for i in range(m):
  a,b = map(int, input().split())
  battery -= a - pre
  if battery <= 0:
    print("No")
    exit()
  # バッテリー容量は超えない
  battery = min(n, battery + (b - a))
  pre = b
print("Yes" if battery - (t - pre) > 0 else "No")