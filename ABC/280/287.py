"""
B問題_Postal Card

積集合
"""

n,m = map(int, input().split())
s = [input()[-3:] for _ in range(n)]
t = set(input() for _ in range(m))

count = 0
for s_i in s:
  if s_i in t: count += 1
print(count)

