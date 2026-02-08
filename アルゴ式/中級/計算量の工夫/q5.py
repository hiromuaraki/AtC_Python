"""
積の総和 (2)
(https://algo-method.com/tasks/16834Gvw)
数え上げ問題（ペア和）
nC2通り = n * (n - 1) // 2!
重複なし
AB + AC + BC
→ A(B + C) + BC
a * (a1 + a2 + a3...an)
"""

n = int(input())
a = list(map(int, input().split()))
s = sum(a)
total = 0
for i in range(n):
  s -= a[i]
  total += a[i] * s
print(total)

# 愚直 0(N^2)
for i in range(n):
  for j in range(i + 1, n):
    total += a[i] * a[j]

