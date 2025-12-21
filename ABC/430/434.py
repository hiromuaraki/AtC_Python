"""
A問題_Balloon Trip・・・解けた
難易度6Q

算数問題
(https://atcoder.jp/contests/abc434/submissions/71303240)
"""

W,B = map(int, input().split())
print((1000*W)//B + 1)

w = W * 1000
n = w // B
for i in range(1, B + 1):
  if n * i < w + n:
    print(n + i)
    exit()


"""
B問題_Bird Watching・・・ギリ解けた
難易度6Q

(https://atcoder.jp/contests/abc434/tasks/abc434_b)

集計（種類ごとの平均値を求める）

合計 / 個数 = 平均値
M行出力

種類ごとの分布をとる
"""

from collections import defaultdict
N,M = map(int, input().split())

sum_a = defaultdict(int)
cnt = defaultdict(int)

for _ in range(N):
  A,B = map(int, input().split())
  sum_a[A] += B
  cnt[A] += 1

for i in range(1, M + 1):
  print(sum_a[i] / cnt[i])



"""
C問題_やらない
"""