"""
B問題_Minesweeper
(https://atcoder.jp/contests/abc075/tasks/abc075_b)
8近傍

上下左右：(i, j) = (行、列)
(-1, 0), (1, 0), (0, -1), (0, 1)

右上右下左下左上
(-1, 1), (1, 1), (1, -1), (-1, -1)

定番テンプレ
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

"""
import copy
h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]
di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, 1, 1, -1, -1]
c = copy.deepcopy(s)

for i in range(h):
  for j in range(w):
    count = 0
    for k in range(8):
      ni, nj = i + di[k], j + dj[k]
      if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == "#":
        count += 1
    if c[i][j] != "#":
      c[i][j] = str(count)
  print("".join(c[i]))

