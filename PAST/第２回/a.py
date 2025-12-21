"""
エレベーター・・・解けた
難しい

データ構造：辞書型
方針：
i<9未満の間は9-iをキーに設定
それ以外はi%9+1をキーに設定し隣接フロアのデータ構造を実装
｜S-T｜の絶対値で隣接フロアの距離を計算
"""

S,T=input().split()
E={}
for i in range(18):
  floor=(f"B{9-i}" if i<9 else f"{i%9+1}F")
  E[floor]=i
print(abs(E[T]-E[S]))
