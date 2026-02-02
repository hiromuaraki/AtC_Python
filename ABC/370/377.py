"""
B問題_Avoid Rook Attack
(https://atcoder.jp/contests/abc377/tasks/abc377_b)

使われていない行＊使われていない列で求める
集合（補集合の問題）
"""

s = [input() for _ in range(8)]

tate = set()
yoko = set()
# 高速な解法（行＊列）
for i in range(8):  
  for j in range(8):
    if s[i][j] == "#":
      tate.add(i) # コマがある行の集合
      yoko.add(j) # コマがある列の集合

print((8 - len(tate)) * (8 - len(yoko)))

# #の行列マスを全て塗り塗られていないの個数を求める
m = [[True] * 8 for _ in range(8)]
lst = []
for i in range(8):  
  for j in range(8):
    if s[i][j] == "#": lst.append((i, j))

for row, col in lst:
  for j in range(8):
    m[row][j] = m[j][col] = False

count = 0
for i in range(8):
  count += sum(m[i])
print(count)