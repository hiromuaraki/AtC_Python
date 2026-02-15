"""
ハッシュの衝突
(https://algo-method.com/tasks/870)
B進数

((c0 * B + c1) * B + c2)

"""

from collections import Counter
import sys

B = 30
M = 1000003

def h(ss: str) -> int:
  words = ss.split()
  lst = []
  for w in words:
    k = 0
    for ch in w:
      # 今の数をB倍して新しい桁を増やす
      k = (k * B + C[ch]) % M
    lst.append(k)
  return max(Counter(lst).values())

C = {chr(ord('a') + i) : i + 1 for i in range(26)}
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

print(h(s))

