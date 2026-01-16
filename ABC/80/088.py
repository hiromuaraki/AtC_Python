"""
B問題_Card Game for Two
"""

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
total = 0
for i in range(n):
  if i % 2 == 0: total += a[i]
  else: total -= a[i]
print(total) 



