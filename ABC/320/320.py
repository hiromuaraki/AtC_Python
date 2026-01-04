"""
A問題_Leyland Number
"""

A,B = map(int, input().split())
print(A**B + B**A)

"""
B問題_
部分文字列の全探索＋回文
(https://atcoder.jp/contests/abc320/tasks/abc320_b)
"""


s = input()
ans = 1
for i in range(len(s)):
  for j in range(len(s)):
    if s[i : j + 1] == s[i: j + 1][::-1]:
      ans = max(ans, len(s[i : j + 1]))
print(ans)