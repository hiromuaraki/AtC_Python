"""
B問題_Nutrients
"""

n,m = map(int, input().split())
a = list(map(int, input().split()))
x = [list(map(int, input().split())) for _ in range(n)]

for j in range(m):
  s = 0
  for i in range(n):
    s += x[i][j]
  if s < a[j]:
    print("No")
    exit()
print("Yes") 