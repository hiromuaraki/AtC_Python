"""
自力AC
1位のチームの正解問題数 max
最終正解時刻 最短 min
"""

N,T = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

x, y = 0, 10**18
for i in range(N):
  q, time = A[i]
  if x < q:
    x = max(x, q)
    y = time
  elif x == q and time <= y:
    y = time

for i in range(N):
  a, b = A[i]
  print(T * (x- a) + (b - y))

