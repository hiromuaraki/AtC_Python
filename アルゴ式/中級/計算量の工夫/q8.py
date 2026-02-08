"""
繁忙期
(https://algo-method.com/tasks/1677R5GX)

累積和の問題（連続するd日間の来場者数の最大の区間を求める）
"""

n,d = map(int, input().split())
x = list(map(int, input().split()))
s = [0] * (n + 1)

for i in range(n):
  s[i + 1] = s[i] + x[i]

mx_visitor = 0
mx_start = 0
for i in range(n - d + 1):
  dist = s[d + i] - s[i]
  if dist >= mx_visitor:
    mx_visitor = dist
    mx_start = i
mx_end = mx_start + d - 1
print(f"{mx_start}~{mx_end}")
  

