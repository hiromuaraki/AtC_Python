"""
キューを配列で実装
(https://algo-method.com/tasks/881dLlu)
queue（キュー）
"""
from collections import deque
n, q = map(int, input().split())

a = [-1] * n
head = tail = 0

for _ in range(q):
  query = list(map(int, input().split()))
  c = query[0]
  if c == 0:
    a[tail] = query[1]
    tail = (tail + 1) % n
  else:
    a[head] = -1
    head = (head + 1) % n

for a_i in a:
  print(a_i)
    
