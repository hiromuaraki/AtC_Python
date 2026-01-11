"""
B問題_Cakes and Donuts
倍数の問題
(https://atcoder.jp/contests/abc105/tasks/abc105_b)
"""

n = int(input())

while n >= 4:
  if n % 4 == 0 or n % 7 == 0:
    print("Yes")
    exit()
  n -= 4
else:
  print("No")