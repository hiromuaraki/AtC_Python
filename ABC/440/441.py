"""
A問題_Black Square
(https://atcoder.jp/contests/abc441/tasks/abc441_a)
難しい


(x,y)行と列が(p,q)の範囲内に収まるか？
"""

p,q = map(int, input().split())
x,y = map(int, input().split())
row = p <= x <= p + 99
column = q <= y <= q + 99
print("Yes" if row and column else "No")

"""
B問題_Two Languages

(https://atcoder.jp/contests/abc441/tasks/abc441_b)
部分集合の問題
文字列集合Sにsが含まれているか？
文字列集合Tにtが含まれているか？

chars ⊆ set_s
（chars は set_s の部分集合）

「使われている文字集合が
どの集合に包含されているか」

set_s <= s
set_t <= t
"""

n,m = map(int, input().split())
set_s = set(input())
set_t = set(input())
q = int(input())

for _ in range(q):
  w = input()
  chars = set(w)
  in_s = chars <= set_s
  in_t = chars <= set_t
  if in_s and in_t:
    print("Unknown")
  elif in_s:
    print("Takahashi")
  else:
    print("Aoki")


"""
C問題_Sake or Water
難易度2Q
(https://atcoder.jp/contests/abc441/tasks/abc441_c)

貪欲法（大きい順から選ぶ）＋ソート
大きい順にして先頭K個を水にし、
最小の酒しか選べないようにする

n-k＝n個のうち既にk個を水にした状態
n-kした状態は、残り小さい容量の酒が残っている

小さい容量のコップだけで、xml以上になるか？

① 高橋くん（プレイヤー）

どのカップを選ぶかを決める
事前に酒の場所は分からない
でも 必ず X ml 以上飲みたい

② 敵（最悪ケース）
酒がどのカップに入っているかを決める
目的：高橋くんが飲む酒を最小にする
制約：酒はちょうど K 個
"""

n,k,x = map(int, input().split())
# 高橋くんが選ぶ酒の容量を最小にするため降順
a = sorted(map(int, input().split()), reverse=True)
total = 0
ans = 0
# n-kの範囲は酒としてカウントしない
# 以降の最小の酒の容量がxml以上になるかを見る
for i in range(n - k, n):
  # 酒になりうる最大範囲だけ加算
  total += a[i]
  if total >= x:
    print(i + 1)
    exit()
print(-1)
