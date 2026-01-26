"""
B問題_Mex
"""


n = int(input())
a = set(map(int, input().split()))
b = list(range(0, max(a) + 2))

for b_i in b:
  if b_i not in a:
    print(b_i)
    exit()