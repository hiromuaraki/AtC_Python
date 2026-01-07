"""
B問題_105
約数の問題
(https://atcoder.jp/contests/abc106/tasks/abc106_b)
"""

n = int(input())
ans = 0
for i in range(1, n + 1):
  if i % 2 == 0: continue
  divisor = 0
  for j in range(1, i + 1):
    if i % j == 0:
      divisor += 1
  if divisor == 8:
    ans += 1
print(ans)