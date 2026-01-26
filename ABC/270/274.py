"""
B問題_Line Sensor
(https://atcoder.jp/contests/abc274/tasks/abc274_b)
グリッド＋縦の計算
"""

h,w = map(int, input().split())
c = [input() for _ in range(h)]
cnt = [0] * w
for i in range(h):
  for j in range(w):
    if c[i][j] == "#": cnt[j] += 1

print(*cnt)