"""
A問題_Raise Both Hands
"""

L,R = map(int, input().split())
if L == R: print("Invalid")
elif L == 1: print("Yes")
else: print("No")


"""
B問題_Binary Alchemy・・・シミュレーション・・・ギリ解けた
難易度84
(https://atcoder.jp/contests/abc370/tasks/abc370_b)

元素＝xの参照先を更新していくことで元素の結合をしている
難しい（問題が抽象的）
"""

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

x = 1
for j in range(N):
  if x > j:
    x = A[x - 1][j]
  else:
    x = A[j][x - 1]
print(x)


"""
問題C_Word Ladder・・・解けない
難易度288

貪欲法

最小回数＋辞書順最小化した文字列を作り出力

・最小回数：文字の異なる個数（ハミング距離）
S!=Tが異なる箇所が入れ替えが発生する最低回数

・辞書順最小化するには
貪欲に先頭の文字を最小化する
その上で2個目以降も順に最小化していき、
min(文字列、文字列)で辞書順の最小化された文字列を取得する



(https://atcoder.jp/contests/abc370/tasks/abc370_c)
"""

S = input()
T = input()
N = len(S)

x = []

# 貪欲法

while S != T: # SとTが等しくなるまで繰り返す
  ns = "z" * N # あり得ない数を設定
  for i in range(N):
    if S[i] != T[i]:
      # 辞書順の最小の文字列を取得
      ns = min(ns, S[:i] + T[i] + S[i + 1:])
  x.append(ns)
  S = ns # 都度最小の文字列に更新する
print(len(x), *x, sep="\n")