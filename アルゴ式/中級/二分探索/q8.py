"""
貯金 (2)
(https://algo-method.com/tasks/366)

Xk ≧ 貯金額になるのは何日目か？
"""

n = int(input())
x = list(map(int, input().split()))
# TLE
for i in range(n):
  k = 0
  day = 1
  # day * (day + 1) // 2 >= xi
  while k + day < x[i]:
    k += day
    day += 1
  print(day)

# d日後の貯金額を求める
# 等差数列の和の公式：S = n / 2(初項＋末項)
def f(d):
  return d * (d + 1) // 2

for i in range(n):
  left = 0
  right = 10**10
  while left < right:
    mid = (left + right) // 2
    if f(mid) >= x[i]:
        right = mid
    else:
        left = mid + 1
  print(left)

