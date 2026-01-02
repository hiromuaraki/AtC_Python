"""
B問題_TAKOYAKI FESTIVAL 2019
n(n - 1) / 2
n個の中から2個たこ焼きを選ぶ
"""
n = int(input())
d = list(map(int, input().split()))
s = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    s += d[i] * d[j]
print(s)

