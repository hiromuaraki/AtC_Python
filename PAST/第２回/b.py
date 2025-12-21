"""
文字列カウント（最多得票数を答える）・・・解けた
"""

S=input()

# 文字a,b,cの個数をそれぞれ数える
a=S.count("a")
b=S.count("b")
c=S.count("c")

# 文字の件数が多い最大値を取得
mx=max(a,b,c)
if mx==a:
  print("a")
elif mx==b:
  print("b")
else:
  print("c")