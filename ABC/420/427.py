"""
A問題_ABC -> AC

文字列の切り取り（スライス）
"""

S = input()
n = len(S) // 2
print(S[:n] + S[n+1:])


"""
B問題_SumOgDigits・・・解けた
難易度54
(https://atcoder.jp/contests/abc427/tasks/abc427_b)

方針
2桁以上の整数は分解して総和する
10 = 1 + 0 = 1
16 = 1 + 6 = 7

予めdigits=1で初期化しておき、
文字列をリストで桁を分解した値を総和する
"""

N = int(input())

digits = 1
for _ in range(N - 1):  
  a = list(str(digits))
  digits += sum(map(int, a))
print(digits)


"""
問題C_Bipartize・・・解説AC
難易度629
(https://atcoder.jp/contests/abc427/tasks/abc427_c)
bit全探索＋二部グラフ

計算量：O(2^NM)
辺で結ばれている全ての頂点の色が異なる
白ー白
黒ー黒などの頂点の組み合わせが存在しないグラフ

頂点の各色を2^N通り試す
頂点の色を塗りわけた時に同じ色で塗られていないグラフ

頂点の色の全探索を行う
・先に頂点の色を決めて色の塗り方を2^N通り試す
・同じ色を結んだ辺を削除
"""

N,M = map(int, input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

ans = 10**4
for i in range(1 << N):
  delete_count = 0
  for v, u in G:
    if 1 & (i >> v) == 1 & (i >> u): # vのフラグの位置をi桁ズラす
      delete_count += 1
  ans = min(ans, delete_count)
print(ans)


"""
D問題_The Simple Game・・・後日やる
難易度981
(https://atcoder.jp/contests/abc427/tasks/abc427_d)
"""