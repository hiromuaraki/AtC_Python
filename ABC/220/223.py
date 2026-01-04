"""
B問題_String Shifting
(https://atcoder.jp/contests/abc223/tasks/abc223_b)

シフト操作するとN回目で必ず1周し元の文字列に戻る（周期性）ため
シフト操作は固定で良い。
"""

s = input()
t = ""
lst = []
lst.append(s)

for i in range(len(s) - 1):
  lst.append(s[i + 1:] + s[:i + 1])
lst.sort()

print(lst[0])
print(lst[-1])

