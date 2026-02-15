"""
逆ポーランド記法の計算
(https://algo-method.com/tasks/67857dY)
"""

from collections import deque

x = input()
n = int(input())
s = list(input().split())
que = deque()
for i in range(n):
  if s[i].isdigit():
    que.append(int(s[i]))
  else:
    n1 = que.pop()
    n2 = que.pop()

    t = 0
    if s[i] == "+": t = n1 + n2
    elif s[i] == "-": t = n2 - n1
    else: t = n1 * n2
    que.append(t)
print(f"{x}={que.pop()}")