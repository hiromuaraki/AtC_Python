"""
B問題_The Middle Day
(https://atcoder.jp/contests/abc315/tasks/abc315_b)
シミュレーション問題
"""

m = int(input())
d = list(map(int, input().split()))
middle = (sum(d)+1) // 2
month, day = 0, 0
total = 0
for i in range(m):
  month = i + 1
  day = middle - total
  total += d[i]
  if middle <= total: break
print(month, day)
