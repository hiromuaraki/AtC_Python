"""
数を選ぶ (2)
(https://algo-method.com/tasks/430)
"""


# DFS解法

def dfs(l, path):
  if len(path) == N:
    return 1
  res = 0
  for i in range(l, R + 1):
    path.append(i)
    res += dfs(i + 1, path)
    path.pop()
  return res
N, L, R = map(int, input().split())
print(dfs(L, []))