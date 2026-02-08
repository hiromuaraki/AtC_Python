"""
方程式を解く
(https://algo-method.com/tasks/368)

二分探索の問題
x(x(x + 1) + 2) + 3 = N

ok/ngの探索範囲の設計が重要
精度は1e-4の範囲までみる

"""
n = float(input())

left= 0
right = 100
while (right - left > 1e-4):
  mid = (left + right) / 2
  if mid * (mid * (mid + 1) + 2) + 3 < n:
    left = mid
  else:
    right = mid
print(left)


