"""
B問題_How many?
(https://atcoder.jp/contests/abc214/tasks/abc214_b)

変数を削る訓練
数式・範囲・場合分け
O(N^3) → O(N^2)へ修正
a + b + c <= s
cが何通りあるか数える

和の制約（Cの取りうる範囲）
c <= s - a - b

a*b*c <= t
積の制約（Cの取りうる範囲）
c <= t // (a * b)

変数を一つ消す＝cの取りうる範囲をまとめて数える
0 ≤ c ≤ min(s - a - b, t / (a*b))

変数が3つ以上ある
制約が「<=」で書かれている
→ 1変数は範囲で数えられる
→ min / max / 場合分け
今回の問題はその 教科書例。
"""

s,t = map(int, input().split())

count = 0
for a in range(s + 1):
  for b in range(s + 1):
    if a + b > s: continue
    if a == 0 or b == 0:
      count += (s - a - b + 1)
    else:
      c_max = min(s - a - b, t // (a * b))
      if c_max >= 0:
        count += (c_max + 1)
print(count)


# 愚直：O(N^3)
# for a in range(s + 1):
#   for b in range(s + 1):
#     for c in range(s + 1):
#       if a + b + c <= s and a*b*c <= t:
#         count += 1
# print(count)
