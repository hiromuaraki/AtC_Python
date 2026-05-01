"""
ライツアウト (1)
(https://algo-method.com/tasks/841)
"""

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
Q = int(input())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
table = [[0] * w for _ in range(h)]

for i in range(h):
  for j in range(w):
    if s[i][j] == "#": table[i][j] = 1

for _ in range(Q):
  query_type, p,q = map(int, input().split())
  count = 0
  for pi, qy in d:
    # マスの存在チェック
    if 0 <= p + pi < h and 0 <= q + qy < w:
      row, col = p + pi, q + qy
      if query_type == 0:
        table[row][col] ^= 1
      else:
        if table[row][col]:
          count += 1
  if query_type == 0:
    table[p][q] ^= 1
  if table[p][q]:
    count += 1
  if query_type == 1:
    print(count)
