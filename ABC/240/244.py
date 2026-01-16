"""
B問題_Go Straight and Turn Right
(https://atcoder.jp/contests/abc244/tasks/abc244_b)

状態をどう持つ？？
方向を辞書で定義
cur：現在の向き

東：0 +1(x)
南：1 -1(y)
西：2 -1(x)
北：3 +1(y)
"""

n = int(input())
t = input()
move = {0: 1, 1: -1, 2: -1, 3: 1}
cur = 0
x_y = [0] * 2
for s in t:
  idx = (0 if cur % 2 == 0 else 1)
  if s == "S":
    x_y[idx] += move[cur]
  else:
    cur = (cur + 1) % 4
print(*x_y)

