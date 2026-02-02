"""
B問題_Inverse Prefix Sum
A1 + A2 + A3...An
累積和の練習問題
"""

n = int(input())
a = list(map(int, input().split()))
s = [0] * n
total = 0
for i in range(n):
  s[i] = a[i] - total
  total += s[i]
print(*s)

