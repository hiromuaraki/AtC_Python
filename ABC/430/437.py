"""
A問題_Feet
"""

a,b = map(int, input().split())
print(a * 12 + b)

"""
B問題_Tombola・・・全探索

setに入れる
O(n^2)
"""

h,w,n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = set(int(input()) for _ in range(n))
ans = 0
for i in range(h):
  count = 0
  for j in range(w):
    if a[i][j] in b:
      count += 1
  ans = max(ans, count)
print(ans)


"""
C問題_Reindeer and Sleigh 2
難易度2Q
(https://atcoder.jp/contests/abc437/tasks/abc437_c)

貪欲法＋ソート

ソリに乗るトナカイの数を最大化させる問題

常に以下の条件が成り立つ
ソリを引くトナカイの総和 ≧ ソリに乗っているトナカイの重さの総和

初期状態は
・全員でソリを引く,そこから1匹ずつソリに乗せる
・コスト小さいトナカイから乗せる
・トナカイをソリに移すときに毎回、力 - P, 重さ + W＝P + W
・ソリに乗せるコスト＝Pi + Wi
・トナカイを何人乗せられるか＝操作回数を最大化できるか？
"""

t = int(input())

# t個のテストケースが与えられる
for _ in range(t):
  n = int(input())
  cost = []
  total_power = 0

  for _ in range(n):
    w, p = map(int, input().split())
    cost.append((p + w, w, p))
    total_power += p # 初期状態はトナカイ全員でソリを引く
  # P＋W：トナカイを乗せるのに必要なコスト
  # Pi+Wiが小さなトナカイから貪欲にソリに乗せるのが最適
  cost.sort()

  power = total_power # 現在の引く力の合計
  weight = 0 # 現在ソリに乗っている重さ
  ans = 0

  for _, w, p in cost:
    # このトナカイをソリに乗せられるか？
    if power - p >= weight + w:
      power -= p
      weight += w
      ans += 1
    # これ以上誰も乗れなくなったら
    else:
      break
  print(ans)


"""
D問題_Sum of Differences
難易度2Q

累積和＋二分探索

bisect_leftとは・・・x ≧ aiの要素の個数を返す関数

(https://atcoder.jp/contests/abc437/tasks/abc437_d)

累積和：
絶対値を式で処理するための記憶装置

left:
x * k：xをk回たす
s[k]：左側要素の合計

right:
s[n] - s[k]：右側要素の合計
x * (n - k)：xを右側の個数分引く
"""

import bisect

n, m = map(int, input().split())
# x未満の要素／x以上の要素に分解し連続した区間にする（絶対値を左右に分解）
a = sorted(map(int, input().split()))
b = list(map(int, input().split()))

MOD = 998244353
s = [0] * (n + 1)

# 累積和を取り区間和をO(1)で取る
for i in range(n):
  s[i + 1] = (s[i] + a[i]) % MOD

ans = 0

for x in b:
  # xより小さい要素の数を返す
  k = bisect.bisect_left(a, x)
  # xをk回足す
  left = (x * k - s[k]) % MOD
  # xを右側の個数分引く
  right = ((s[n] - s[k]) - x * (n - k)) % MOD
  ans += (left + right) % MOD
print(ans % MOD)