"""
総和クエリ (1)
(https://algo-method.com/tasks/991yuE2)

累積和の問題
計算量：O(N + Q)
"""

n = int(input())
a = list(map(int, input().split()))
q = int(input())
s = [0] * (n + 1)

for i in range(n):
  s[i + 1] = s[i] + a[i]

for _ in range(q):
  print(s[int(input())])