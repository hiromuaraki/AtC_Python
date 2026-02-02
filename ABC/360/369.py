"""
A問題_369
6Q
(https://atcoder.jp/contests/abc369/tasks/abc369_a)
少し難しい
等差数列の関係式
x = 2A - B
x = A + b / 2
x = 2B - A
"""

a,b = map(int, input().split())
if a == b: print(1)
elif (a + b) % 2 == 0: print(3)
else: print(2)


"""
B問題_Piano
(https://atcoder.jp/contests/abc369/tasks/abc369_b)
シミュレーション問題

必要な変数
L,Rの疲労度
前回の銀盤の位置

"""
n = int(input())
acc = [0] * 2
hand = [0] * 2
idx = {"L": 0, "R": 1}

dist, total = 0, 0
for _ in range(n):
  a,s = input().split()
  a = int(a)
  move = idx[s]
  hand[move] += 1
  dist = abs(a - acc[move])
  acc[move] = a
  if hand[move] >= 2:
    total += dist
print(total)

