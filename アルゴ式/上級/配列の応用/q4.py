"""
先頭への挿入
(https://algo-method.com/tasks/832)
"""

from collections import deque
n = int(input())
a = list(map(int, input().split()))
q = int(input())

que = deque(a)
while q > 0:
  q -= 1
  query_type = list(map(int, input().split()))
  if query_type[0] == 0:
    que.appendleft(query_type[1])
  else:
    print(que.popleft() if que else "Error")