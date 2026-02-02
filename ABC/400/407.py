"""
B問題_P(X or Y)
"""

x,y = map(int, input().split())

count = 0
for a in range(1, 7):
  for b in range(1, 7):
    if a + b >= x or abs(a - b) >= y:
      count += 1
print(count / 36)