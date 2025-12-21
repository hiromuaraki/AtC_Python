"""
A問題_Permute to Maximize・・・解けた
難易度
"""

A = sorted(map(int, input().split()), reverse=True)
print("".join(map(str, A)))

"""
B問題_Permute to Minimize・・・解けた
難易度？？

数理化構造に落とし込まないとダメ

あらかじめ昇順に並び替えておき、
0が先頭の時のみ最初に見つかった0でない整数と入れ替え結果を出力
"""

X = sorted(map(int, input()))

if X[0] == 0:
  for i in range(1, len(X)):
    if X[i] != 0:
      X[0], X[i] = X[i], X[0]
      break
print("".join(map(str, X)))


# 順列全探索ver → これは無駄なコード

import itertools
from collections import Counter
A = list(map(int, input()))

counter = Counter(A)
if counter[0] == 0:
  A = sorted(A)
  print("".join(map(str, A)))
  exit()

ans = 10**5+1
for a in itertools.permutations(A, len(A)):
  if a[0] == 0: continue
  num = int("".join(map(str, a)))
  if num < ans:
    ans = num
print(ans)

"""
C問題_Candy Tribulation・・・解けない

今の自分でレベルでは解けない
Novistepsで数理化思考を鍛えて再チャレンジ
https://atcoder.jp/contests/abc432/tasks/abc432_c
"""