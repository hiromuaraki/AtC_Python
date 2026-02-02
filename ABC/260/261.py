"""
B問題_Tournament Result
(https://atcoder.jp/contests/abc261/tasks/abc261_b)

総当たり戦の結果が矛盾しているか
OKな組合せ：WL, LW, DD
NG：それ以外
"""

n = int(input())
a = [list(input()) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j: continue
    if a[i][j] + a[j][i] not in ("WL", "LW", "DD"):
      print("incorrect")
      exit()
print("correct")

    

