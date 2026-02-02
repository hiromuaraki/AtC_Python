"""
A問題_Grandma's Footsteps
(https://atcoder.jp/contests/abc428/tasks/abc428_a)
難しい
周期性もしくはシミュレーション

a：走る
b：止まる
a + b：走る＋静止
s * a = 距離
x // (a + b)： a + bの一つのブロックがx秒間何個あるか？
x % (a + b)：x秒間のなかにあるa + bのブロックのあまり数＝残り時間

a秒以上か、未満かで場合分け
min(a, x % (a + b) * s)
→走れる時間は最大a秒まで
超えた場合は、a秒をかける
a秒未満は、サイクルのあまり時間をかける
"""

s,a,b,x = map(int, input().split())
# 周期性を利用した解法
print(s * a * (x // (a + b)) + min(a, x % (a + b)) * s)

# シミュレーション
ans = 0
for time in range(x):
  if time % (a + b) < a:
    ans += s
print(ans)