"""
(https://atcoder.jp/contests/abc122/tasks/abc122_b)
部分文字列の全探索（部分集合）
l < r <= n（末尾含む）
ACGT以外の文字列が含まれない区間の最大長を求める

左端固定＋右端拡張
"""

s = input()
n = len(s)
t = {"A", "C", "G", "T"}

count = 0
# 愚直解法
# for l in range(n):
#   for r in range(l, n + 1):
#     acgt = set(s[l : r]) - t
#     if len(acgt) != 0: break
#     count = max(count, len(s[l : r]))
# print(count)

l = 0
for r in range(n):
  if s[r] not in t:
    l = r + 1
  else:
    count = max(count, r - l + 1)
print(count)