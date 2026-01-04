"""
A問題_2^n - 2*n
"""

n = int(input())
print(2**n - 2*n)


"""
B問題_Happy Number
難易度4Q（Bにしては難しい）やるだけではない
(https://atcoder.jp/contests/abc439/tasks/abc439_b)

桁分解＋総和のシミュレーション¥
ハッピー数にならないケース＝総和が重複した値を繰り返すとき

問題文をちゃんと読み読解＆繰り返しているデータの性質を見抜く
"""

n = int(input())
total = n
st = set()

while total != 1:
  if total in st:
    print("No")
    break
  st.add(total)
  total = sum(int(digit)**2 for digit in str(total))
else:
  print("Yes")

"""
C問題_2026
難易度2Q

境界問題＋全探索
(https://atcoder.jp/contests/abc439/tasks/abc439_c)

x*x + y*y <= nの(x, y)の組で
出現回数が1回の(x, y)の組を分布取り出力する

(x, y)の組を全探索で全列挙
x^2 + y^2 <= nとは

x^2 <= n かつ y^2 <= nが必須条件
なので探索範囲は
x^2 + y^2 <= √Nまででいい

x,yいずれかが√Nを超えた時点でその(x, y)組みはNにはならないため全探索の意味がない
√Nは、x^2 + y^2 = nの OK／NGが切り替わる境界
境界条件は x*x + y*y > nに設定
ある地点までOK,ある地点からNGは単調性がある＝思考構造は二分探索と同じ
"""

n = int(input())
cnt = [0] * (n + 1)

limit = int(n**0.5)

for x in range(1, limit + 1):
  for y in range(x + 1, limit + 1):
    sq = x*x + y*y
    if sq > n:
      break
    # 良い整数の条件は出現回数が1回のため
    # nごとの出現回数を数えて1回の出現のみを昇順で出力
    cnt[sq] += 1

good = [i for i, v in enumerate(cnt) if v == 1]
print(len(good))
print(*good)