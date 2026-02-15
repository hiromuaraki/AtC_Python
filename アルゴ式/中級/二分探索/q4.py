"""
小さい数の個数
(https://algo-method.com/tasks/382)
Ax ≦ Biの（境界）を探す＝個数を数える
"""
import bisect
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = list(map(int, input().split()))

# Ax ≦ Biの個数を数える
# bisect_rightの解法
for b_i in b:
  print(bisect.bisect_right(a, b_i))

for b_i in b:
  left, right = 0, n
  while left != right:
    mid = (left + right) // 2
    if a[mid] <= b_i:
      left = mid + 1
    else:
      right = mid
  print(left)


