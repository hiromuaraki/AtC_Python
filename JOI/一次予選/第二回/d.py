n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
score = 0
for i in range(n):
  score += a[i]
  score = score if score not in b else 0
print(score)


"""
2022
難しい
"""

from collections import Counter
n = int(input())
a = list(map(int, input().split()))
counter = Counter(a)
min_n = 10**9
ans = 10**9
for k,v in sorted(counter.items(), key=lambda x : x[1]):
  if v <= min_n:
    min_n = v
    ans = min(ans, k)
print(ans)