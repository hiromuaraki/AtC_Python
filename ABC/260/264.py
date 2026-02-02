"""
B問題_Nice Grid
チェビシェフ距離の問題
(https://atcoder.jp/contests/abc264/tasks/abc264_b)

中心点（8, 8）からの距離をチェス盤距離で計算

白→黒→白→黒→白→黒→白→黒(0,1,2,3,4,5,6,7) = 8個
偶奇に着目する
"""

r,c = map(int, input().split())
# 中心（8,8）からの距離を求める
if max(abs(r - 8), abs(c - 8)) % 2 == 0:
  print("white")
else:
  print("black")