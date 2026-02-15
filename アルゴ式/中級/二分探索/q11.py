"""
九九の表（１）
(https://algo-method.com/tasks/406)
"""

n, k = map(int, input().split())
count = 0
for i in range(n):
  # j <= k//(i + 1)
  # kの中にj以下がいくつあるか
  count += min(n, k // (i + 1))
print(count)
