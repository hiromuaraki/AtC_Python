"""
A問題_Stage Clear
"""

i,j = map(int, input().split("-"))
if j < 8:
  j += 1
elif i < 8 and j == 8:
  i += 1; j = 1
print(i, j, sep="-")


"""
B問題_Looped Rope・・・解けた
難易度６Q

グリッド問題＋上下左右の範囲外を制御
"""


H,W = map(int, input().split())
S = [input() for _ in range(H)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

x, y = 0, 0
for i in range(H):
  for j in range(W):
    if S[i][j] == ".": continue
    count = 0
    for dy, dx in d:
      y = dy + i ; x = dx + j
      if 0 <= y < H and 0 <= x < W:
        if S[y][x] == "#":
          count += 1
    if count not in (2, 4):
      print("No")
      exit()
print("Yes")


"""
C問題_AtCoder AAC Contest・・・解けない
難易度２Q
(https://atcoder.jp/contests/abc422/tasks/abc422_c)
  
二分探索の問題
・判定問題
・単調増加／単調減少
・最大のTrueを探す

x回コンテストを開催できるか／できないかの２択（単調性）
＝Yes／Noで考えられる

1) x <= a
2) x <= c
3) 3x <= a + b + c


・nA ≧ x・・・”A”の数制限
・nC ≧ x・・・”C”の数制限
・(nA - x) + (nC - x) + b ≧ x・・・文字全体の数制限
→各コンテストで3文字使う＝3x文字使う

文字の総数＝nA + nB + nC 

解法１：二分探索（判定問題＋単調性）
x回開催できる最大の境界を調べる（単調性あり）
f(x) が “True → False” と一回だけ切り替わる単調性を持つこと


解法２
算数
min(nA, nC, (nA + nC + nB) // 3)
"""

T = int(input())

def jude(x, a, c):
  # x回コンテストを開くため最低限必要なAがx個、Cがx個 
  if x > min(a, c):
    return False
  # その後に残る文字総数（A + B + C の残り）が x 個以上あるか？
  return (a - x) + b + (c - x) >= x

# x回のコンテストを開催できるかを判定し
# x回開催できる最大の境界を調べる
for _ in range(T):
  a, b, c = map(int, input().split())
  ok = 0; ng = 10**9+1
  while ng - ok > 1:
    mid = (ok + ng) // 2
    if jude(mid, a, c):
      ok = mid
    else:
      ng = mid
  print(ok)


# 別解
"""
二分探索がしていることは下記条件1〜条件3までを満たす最大の境界xを探している
＝TrueがFalseに切り替わる境界を探している

条件1：Aが足りている x <= A
条件2：Cが足りている x <= C
条件3：最低限必要な 2x個のAとCを確保した後残りの文字数
(a - x) + (c - x) + b = (a + b + c)-2x

(a + b + c)-2x ≧ x個以上必要
3x ≦ (a + b + c)
x = (a + b + c) // 3

""" 
for _ in range(T):
  a,b,c = map(int, input().split())
  print(a, c, (a + b + c) // 3)
