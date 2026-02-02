"""
B問題_Let's Get a Perfect Score
(https://atcoder.jp/contests/abc282/tasks/abc282_b)

for文の設計が若干めんどくさい
"""

n,m = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
for i in range(n):
  for j in range(i + 1, n):
    ok = True
    for k in range(m):
      if s[i][k] == s[j][k] == "x":
        ok = False
        break
    if ok:
      ans += 1
print(ans)