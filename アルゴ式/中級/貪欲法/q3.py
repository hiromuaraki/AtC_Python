"""
コイン問題
(https://algo-method.com/tasks/360)

a,b,c,d：使える枚数
50円->10円->5円->1円

少し頭の整理が必要
x円の中でコインが何枚使えるか
使える枚数の上限はそれぞれ与えられるa,b,c,d
"""

x = int(input())
a,b,c,d = map(int, input().split())
coins = map(int, input().split())
values = [50, 10, 5, 1]

# ループで抽象化③
# 値と枚数を配列化
# zipで処理
# 最も構造的
ans = 0
for coin, val in zip(coins, values):
  use = min(coin, x // val)
  ans += use
  x -= use * val
print(ans)



# 処理の共通部分をまとめた
# 可読性は向上
# でも種類ごとの呼び出しは手動
x = int(input())
a,b,c,d = map(int, input().split())
a50 = b10 = c5 = d1 = 0
# 関数化②
def greedy(min_num: int, t: int):
  global x
  coin = min(min_num, x // t)
  x -=  t * coin
  return coin

ans = 0
ans += greedy(a, 50)
ans += greedy(b, 10)
ans += greedy(c, 5)
ans += greedy(d, 1)
print(ans)



x = int(input())
a,b,c,d = map(int, input().split())
a50 = b10 = c5 = d1 = 0


# 個別処理①
# 50 → 10 → 5 → 1 を順番に処理
# 直感的だが冗長
# 抽象化されていない
a50 = min(a, x // 50)
x = min(x, x - (50 * a50))
b10 = min(b, x // 10)
x = min(x, x - (10 * b10))
c5 = min(c, x // 5)
x = min(x, x - (5 * c5))
d1 = min(d, x // 1)
x = min(x, x - (d * d1))
print(a50 + b10 + c5 + d1)