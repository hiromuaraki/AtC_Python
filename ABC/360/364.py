"""
B問題_Grid Walk
グリッドの問題：4近傍
(https://atcoder.jp/contests/abc364/tasks/abc364_b)
"""

h,w = map(int, input().split())
si,sj = map(int, input().split())
c = [input() for _ in range(h)]
x = input()
d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)} # 上下左右

si -= 1; sj -= 1
for move in x:
  di,dj = d[move]
  # マスの存在チェック
  ni,nj = si + di, sj + dj
  if 0 <= ni < h and 0 <= nj < w:
    if c[ni][nj] == ".":
      si = ni; sj = nj

print(si + 1, sj + 1)
  
