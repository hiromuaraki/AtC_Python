"""
B問題_美しい文字列
"""
from collections import Counter
w = input()
counter = Counter(w)
if all(v % 2 == 0 for k,v in counter.items()):
  print("Yes")
else:
  print("No")