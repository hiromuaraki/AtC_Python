"""
B問題_Overlapping sheets
(https://atcoder.jp/contests/abc318/tasks/abc318_b)
難しい＝マスを塗って塗った個数を数える問題

diff101
グリッド＋シミュレーション＋和集合

マスの個数を数える問題に思考変換しないと永遠に解けない

座標平面上の各地点について、
少なくとも1枚の長方形の内部に含まれている地点の集合
の面積を求めよ

(B - A) * (C - D)：各シートがどのマスを覆うかを決めるための範囲指定

**「1枚以上のシートに覆われている面積」
「1回でも塗られたマスの総数」**


"""

n = int(input())
covered = [[False] * 101 for _ in range(101)]

for _ in range(n):
  a,b,c,d = map(int, input().split())
  for x in range(a, b):
    for y in range(c, d):
      covered[x][y] = True

count = 0
for i in range(101):
  for j in range(101):
    if covered[i][j]: count += 1
print(count)





