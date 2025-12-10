"""
問題_013_Divisor Enumeration・・・解けた
難易度5Q

約数列挙

1..√N回まわる
"""

N = int(input())
ans = []
# 1..√N回まわる
for i in range(1, int(N**0.5) + 1):
  if N % i != 0:
    continue
  ans.append(N // i)
  if N // i != i:
    ans.append(i)
print(*sorted(ans), sep="\n")