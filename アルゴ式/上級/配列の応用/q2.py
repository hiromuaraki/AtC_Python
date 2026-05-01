"""
ままこだて
(https://algo-method.com/tasks/833)
"""

n = int(input())
a = [i + 1 for i in range(n)]
while len(a) != 1:
  a.pop(0)
  a.append(a[0])
  a.pop(0)
print(*a)

