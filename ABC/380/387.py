"""
A問題_Happy New Year 2025
"""

A,B = map(int, input().split())
print((A + B)**2)


"""
B問題_ 9x9 Sum・・・解けた
難易度21
"""

X = int(input())
total = 0
for i in range(1, 10):
  for j in range(1, 10):
    if i * j != X:
      total += i * j
print(total)


"""
C問題_Snake Numbers・・・解けない後日復習
難易度1249
(https://atcoder.jp/contests/abc387/tasks/abc387_c)

解法が全く分からない
10 ≦ L ≦ R ≦ 10^18
L以上R以下の中で先頭の桁がどの桁よりも大きい個数を求める

今の自分では理解できない
"""

