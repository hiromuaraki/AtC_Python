"""
B問題_Frequency
"""

from collections import Counter
s = input()
counter = Counter(s)
ans = ""
value = 0
for k,v in counter.items():
  if value < v:
    value = v
    ans = k
  elif value == v:
    ans = min(ans, k)
print(ans)