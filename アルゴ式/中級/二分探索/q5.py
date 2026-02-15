"""
和が K 以上のペア
(https://algo-method.com/tasks/381)
Ai + Aj ≧ kを満たす(i, j)の組を求める
32bit整数(int型)には収まらないためlong(64bit)で対応

Ai + Aj ≧ k
Aj ≧ k - Aiに式変形できる。Ajの取りうる範囲
Aj ≧ k - Aiが成り立つAjがいくつあるか？
"""

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
count= 0
for i in range(n):
  left, right = 0, n
  # 二分探索：解が求まるまで
  while right != left:
    mid = (left + right) // 2
    if a[mid] >= k - a[i]:
      right = mid
    else:
      left = mid + 1
  count += n - left
print(count)

