"""
ハッシュ

計算量：O(N＋Q）
"""
from collections import  defaultdict
n = int(input())
s = list(input().split())
q = int(input())

counter = defaultdict(int)
for i in range(n):
  counter[s[i]] += 1

for _ in range(q):
  t = input()
  print(counter[t] if counter[t] else 0)
    
