"""
駅と駅の距離
(https://algo-method.com/tasks/585WM5q)
"""

n = int(input())
d = list(map(int, input().split()))
q = int(input())
s = [0] * n
for i in range(n - 1):
  s[i + 1] = s[i] + d[i]

for _ in range(q):
  l,r = map(int, input().split())
  print(s[r] - s[l])