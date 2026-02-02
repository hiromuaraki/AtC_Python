"""
B問題_Visibility
(https://atcoder.jp/contests/abc197/tasks/abc197_b)

4近傍
"""

h,w,x,y = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
count = 1

s = [input() for _ in range(h)]
x -= 1; y -= 1
for i in range(4):
  ni, nj = x + dy[i], y + dx[i]
  while (0 <= ni < h and 0 <= nj < w) and s[ni][nj] != "#":
    count += 1
    ni += dy[i]
    nj += dx[i]
print(count)

