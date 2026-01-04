"""
B問題_You're a teapot
部分文字列＋全探索
(https://atcoder.jp/contests/abc418/tasks/abc418_b)
"""

s = input()
n = len(s)
ans = 0
for l in range(n):
  if s[l] != 't': continue
  for r in range(l + 2, n):
    if s[r] != 't': continue
    length = r - l + 1
    x = s[l : r + 1].count('t')
    ans = max(ans, (x - 2) / (length - 2))
print(ans)