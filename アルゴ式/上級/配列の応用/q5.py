"""
両端への挿入
(https://algo-method.com/tasks/834)
"""
from collections import deque
n = int(input())
a = list(map(int, input().split()))
q = int(input())
que = deque(a)
while q > 0:
  q -= 1
  query_type, k = map(int, input().split())
  if query_type == 0:
    que.appendleft(k)
  elif query_type == 1:
    que.append(k)
  else:
    print(que[k] if len(que) > k else "Error")
    