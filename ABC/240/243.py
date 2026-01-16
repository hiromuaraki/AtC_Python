"""
A問題_Shampoo
シミュレーション＋周期性の問題

父＞母＞高橋くんの3周期

周期性で考えた時に、1日でa + b + cのシャンプー量がvから減る
v % (a + b + c)
25 % 33 = 25
v < 10：F
v < a + b：M
その他：T
"""

lst = list(map(int, input().split()))
v,a,b,c = map(int, input().split())

# 場合分け
if v < a: print("F")
elif v < a + b: print("M")
else: print("T")

dict = {0: "F", 1: "M", 2: "T"}
v, a = lst[0], lst[1:]
i = 0
# シミュレーション
while v >= a[i]:
  v -= a[i]
  i = (i + 1) % len(a)
print(dict[i])
