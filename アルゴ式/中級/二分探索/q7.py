"""
段階評価
(https://algo-method.com/tasks/671eed91313e9d35)

Xi > Aiの最大のインデックス（境界）を探す
"""

import bisect
n, k = map(int, input().split())
a = list(map(int ,input().split())) 
x = list(map(int ,input().split()))

# Xi > Aiを満たす最大のインデックスを探す
for i in range(n):
  print(bisect.bisect_right(x, a[i]))

# 別解
for i in range(n):
  left = 0
  right = k
  while left < right:
    mid = (left + right) // 2
    if x[mid] <= a[i]:
      left = mid + 1
    else:
      right = mid
  print(left)
