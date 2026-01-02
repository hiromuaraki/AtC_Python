"""
アルゴリズムと数学
034 - Nearest Points

ユークリッド距離（斜めの最も近い距離を求める）
√(x1 - x2)^2 + (y1 - y2)^2

"""

n = int(input())
d = list(tuple(map(int, input().split())) for _ in range(n))

def dist(a, b):
  x1, y1 = a
  x2, y2 = b
  return (((x1 - x2)**2) + ((y1 - y2)**2))**0.5

min_dist = 10**9
for i in range(n - 1):
  for j in range(i + 1, n):
    min_dist = min(min_dist, dist(d[i], d[j]))
print(min_dist)


