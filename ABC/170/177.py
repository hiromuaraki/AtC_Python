"""
B問題_SubString
部分文字列+全探索
(https://atcoder.jp/contests/abc177/tasks/abc177_b)
"""

s = input()
t = input()

ans = 10**9
for i in range(len(s) - len(t) + 1):
  diff_count = 0
  k = s[i : len(t) + i]
  for j in range(len(t)):
    if k[j] != t[j]: diff_count += 1
  ans = min(ans, diff_count)
print(ans)