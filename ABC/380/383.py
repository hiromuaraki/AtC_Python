"""
A問題_Humidifier 1
(https://atcoder.jp/contests/abc383/tasks/abc383_a)
シミュレーション問題（難しい）6Q

必要な変数
前の時間 = 0
水の量 = 0

前の時刻の保持時に、maxを設定し、負の値を0に制御
max(0, 水の量 - (現在の時刻 - 前の時刻))で水の量の状態を管理
負の場合：0
正の場合：水の量 - (現在の時刻 - 前の時刻)
"""

n = int(input())

water, time = 0, 0
for i in range(n):
  t,v = map(int, input().split())
  water = max(0, water - (t - time))
  water += v
  time = t
print(water)