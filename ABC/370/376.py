"""
A問題_Candy Button
(http://atcoder.jp/contests/abc376/tasks/abc376_a) 

必要な変数
前回あめをもらった時間
あめの個数
"""

n,c = map(int, input().split())
t = list(map(int, input().split()))

pre_t = 0
candy = 1
for i in range(n - 1):
  if t[i + 1] - t[pre_t] < c: continue
  pre_t = i + 1
  candy += 1
print(candy)
  

