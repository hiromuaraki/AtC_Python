"""
A問題_Exponential Plant
(https://atcoder.jp/contests/abc354/tasks/abc354_a)
シミュレーション
"""

h = int(input())
c = 0
ans = 0
for i in range(h + 1):
  c += 2**i
  if c > h:
    ans = i + 1
    break
print(ans)