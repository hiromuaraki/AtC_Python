"""
最小の添字
(https://algo-method.com/tasks/370)

Ax ≧ Biになる最小のインデックス（境界）を探す
"""

import bisect
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# Ax ≧ biの最小の境界(インデックス)を探す
# bisect_leftの解法
for b_i in b:
  print(bisect.bisect_left(a, b_i))

for b_i in b:
  left, right = 0, n
  # 答えが見つかるまで最小のインデックスを探す
  while left != right:
    mid = (left + right) // 2
    if a[mid] >= b_i:
      right = mid
    else:
      left = mid + 1
  print(left)