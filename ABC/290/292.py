"""
B問題_Yellow and Red Card
"""

n,q = map(int, input().split())
player = [0] * n

for _ in range(q):
  c,x = map(int, input().split())
  x -= 1
  if c == 1:
    player[x] += 1
  elif c == 2:
    player[x] = -1
  else:
    print("Yes" if player[x] in (2, -1) else "No")

