"""
B問題_Two Anagrams
diff 497（茶）
辞書順の問題
昇順＜降順すればいい
(https://atcoder.jp/contests/abc082/tasks/abc082_b)

辞書順とは
左から1文字ずつ文字コート順に比較を行い最初に異なる文字が出た時点で、
最小を確定させるアルゴリズム。

for i in range(len):
    if s[i] != t[i]:
        return s[i] < t[i]


もし片方がもう一方の先頭部分と完全に一致する場合、文字数が少ない方が先になる。
"""

s = "".join(sorted(input()))
t = "".join(sorted(input(), reverse=True))
print("Yes" if s < t else "No")
  