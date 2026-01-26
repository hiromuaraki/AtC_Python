"""
B問題_Election
"""

from collections import defaultdict
n = int(input())
d = defaultdict(int)

for _ in range(n):
  d[input()] += 1

mx = 0
ans = ""
for k,v in d.items():
  if mx < v:
    mx = v
    ans = k
print(ans)