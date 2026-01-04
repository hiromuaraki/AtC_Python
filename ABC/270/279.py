"""
B問題_LOOKUP
(https://atcoder.jp/contests/abc279/tasks/abc279_b)
連続部分文字列の全探索
"""


s = input()
t = input()

if s == t:
  print("Yes")
  exit()

for i in range(len(s) - len(t) + 1):
  x = ""
  for j in range(len(t)):
    x += s[i + j]
  if x == t:
    print("Yes")
    exit()
print("No")