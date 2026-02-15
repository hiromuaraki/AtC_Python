"""
タスクリスト (Hard)
(http://algo-method.com/tasks/940HGrR)

削除しながら回すならwhile
"""

from collections import deque

x = int(input())
q = int(input())
tasks = deque()
count = 0
for _ in range(q):
  c,t = map(int, input().split())
  if c == 0:
    tasks.append(t + x)
  else:
    while tasks and tasks[0] <= t:
      tasks.popleft()
      count += 1
    print(count)

    
