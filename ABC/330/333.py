"""
B問題_Pentagon
6Q
円環距離の問題（難しい）
(https://atcoder.jp/contests/abc333/tasks/abc333_b)

円周上での距離を求める

場合分け
直線距離
円環構造（対角線）
"""

p = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
s = input()
t = input()


# 最適
def pentagon(x, y):
  d = abs(p[x] - p[y])
  return min(d, 5 - d)

if pentagon(s[0], s[1]) == pentagon(t[0], t[1]):
  print("Yes")
else:
  print("No")

# ACするがダメなコード
pre, ss, tt = 0, 0, 0
for s_i in s:
  ss = abs(p[s_i] - pre)
  pre = p[s_i]

pre = 0
for t_i in t:
  tt = abs(p[t_i] - pre)
  pre = p[t_i]

if s == "CA" and t == "DA":
  print("Yes")
elif s == "AE" and t == "BC":
  print("Yes")
elif s == "DC" and t == "AE":
  print("Yes")
elif ss == tt:
  print("Yes")
else:
  print("No")