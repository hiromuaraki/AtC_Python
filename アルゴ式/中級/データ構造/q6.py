"""
タスクリスト
(https://algo-method.com/tasks/613Zsiv)
"""

from collections import deque
q = int(input())
tasks = deque()
for _ in range(q):
  query = input().split()
  c = query[0]
  if c == "0":
    tasks.append(query[1])
  else:
    print(tasks.popleft())