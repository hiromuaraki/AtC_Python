"""
B問題_Two Colors Card Game

diff319
"""
from collections import defaultdict
n = int(input())
m = int(input())
counter = defaultdict(int)

for _ in range(n):
  s = input()
  counter[s] += 1

for _ in range(m):
  t = input()
  counter[t] -= 1
print(max(max(counter.values()), 0)) 