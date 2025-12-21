"""
辞書順に並べ替える
注）大文字小文字のケース無視（人間のイメージする辞書順）
機械的ではない辞書順

key=str.lower
全て小文字に変換し並べ替える（元文字列は変わらない）
"""

S = list(input())
t = ""
count = 0

for s in S:
    t += s
    if s.isupper():
        count += 1
    if count == 2:
        t += ","
        count = 0

l = t.split(",")
# 空要素を取り除く
l = [word for word in l if word]

# 単語ごとに辞書順に並べ替えて、区切り無しで連結
print("".join(sorted(l, key=str.lower)))