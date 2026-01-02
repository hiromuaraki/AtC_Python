"""
091 - How Many Ways?

a, bが決まればcも決まる
a + b + c = x
c = x - a - b

cがn以下の範囲
かつ
a < b < cの条件を満たす範囲

b < c <= n
"""

n,x = map(int, input().split())
ans = 0

# O(N^3)
for a in range(1, n):
  for b in range(a + 1, n):
    for c in range(b + 1, n):
      if a + b + c == x: ans += 1

# O(N^2)
for a in range(1, n):
  for b in range(a + 1, n):
    c = x - a - b
    if b < c <= n: ans += 1
print(ans)