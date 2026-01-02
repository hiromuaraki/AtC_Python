"""
B問題_Default Price
"""

n, m = map(int, input().split())
c = list(input().split()) # 食べた皿の色
d = list(input().split()) # 対応する皿の色
p = list(map(int, input().split())) # 値段

price = {color : p[i + 1] for i, color in enumerate(d)}
total = 0
for c_i in c:
  if c_i in price:
    total += price[c_i]
  else:
    total += p[0]
print(total)