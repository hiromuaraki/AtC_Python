"""
B問題_Pasta
"""
from collections import Counter
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

counter = Counter(a)
for b_i in b:
  if counter[b_i] == 0:
    print("No")
    exit()
  counter[b_i] -= 1
print("Yes")