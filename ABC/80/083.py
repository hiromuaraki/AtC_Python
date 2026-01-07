"""
B問題_Some Sums
"""

n,a,b = map(int, input().split())
s = 0
for i in range(1, n + 1):
  str_n = sum(list(map(int, str(i))))
  if a <= str_n <= b:
    s += i
print(s)