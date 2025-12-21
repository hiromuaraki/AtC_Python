"""
A問題_o-padding
"""

n = int(input())
s = input()
print("o"*(n - len(s)) + s)


"""
B問題_MagicSquare
少し難しい
問題の意図がわかりずらい
"""

n = int(input())
g = [[0] * n for _  in range(n)]

r = 0
c = (n - 1) // 2 
g[r][c] = 1

for k in range(2, n * n + 1):
  x = (r - 1) % n
  y = (c + 1) % n
  if g[x][y] == 0:
     r, c = x, y
  else:
    r = (r + 1) % n
  g[r][c] = k

for i in range(n):
  print(*g[i])


"""
C問題_2x2 Placing
難易度
"""

n, m = map(int, input().split())
st = set()
ans = 0
for _ in range(m):
  r, c = map(int, input().split())
  r -= 1; c -= 1
  if(r, c) in st: continue
  if (r, c + 1) in st: continue
  if (r + 1, c) in st: continue
  if (r + 1, c + 1) in st: continue
  st.add((r, c))
  st.add((r, c + 1))
  st.add((r + 1, c))
  st.add((r + 1, c + 1))
  ans += 1
print(ans)