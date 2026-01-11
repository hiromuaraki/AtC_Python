"""
B問題_1%
少し難しい
(https://atcoder.jp/contests/abc165/tasks/abc165_b)

"""
x = int(input())
a = 100
year = 0

while a < x:
  a += a // 100
  year += 1
print(year)