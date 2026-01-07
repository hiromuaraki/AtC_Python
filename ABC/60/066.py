"""
B問題_ss
文字列切り取り＋全探索
インデックスの左右の境界をバグらせないように事前に切り取り位置の設計
(https://atcoder.jp/contests/abc066/tasks/abc066_b)
"""

s = input()
n = len(s)

ans = 1
for i in range(n):
  t = s[:n - 1 - i]
  slice = len(t)
  if slice % 2 == 0:
    if t[0 : slice // 2] == t[slice // 2 :]:
      ans = slice
      break
print(ans)
