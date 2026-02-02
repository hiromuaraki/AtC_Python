"""
B問題_CTZ

binを使う
"""

n = int(input())
n = bin(n)

ans = 0
for i in n[::-1]:
  if i != "0": break
  ans += 1
print(ans)
