"""
3つの数の和
(https://algo-method.com/tasks/877AFBj)
x,y,zの組
数え上げの問題
z回回さずzの個数を数える
和の制約
x + y + z <= m
z <= m - x - y

zの取りうる範囲
1 <= z <= min(n, m - x - y)
x, y が固定されたときに、和の制約から許される z の最大値

個数=min(n,m−x−y)
"""

n,m = map(int, input().split())
count = 0
for x in range(1, n + 1):
  for y in range(1, n + 1):
    count += max(0, min(n, m - x - y))
print(count)