"""
総和クエリ (1)
(https://algo-method.com/tasks/990s6ea)

累積和（区間差の問題）
"""

n = int(input())
a = list(map(int, input().split()))
q = int(input())
s = [0] * (n + 1)

for i in range(n):
  s[i + 1] = s[i] + a[i]

for _ in range(q):
  l,r = map(int, input().split())
  print(s[r] - s[l])


