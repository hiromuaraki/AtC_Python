"""
B問題_Savings
"""

n = int(input())
s = 0
ans = 0
for i in range(1, n + 1):
  s += i
  ans = i
  if s >= n: break
print(ans)