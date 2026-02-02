"""
A問題_Shout Everyday
6Q
難しい
(https://atcoder.jp/contests/abc367/tasks/abc367_a)

日を跨ぐ場合と、日を跨がないで場合分け
"""

a,b,c = map(int, input().split())

# 日を跨いでいない場合
if b < c:
  if c < a or a < b: print("Yes")
  else: print("No")
# 日を跨いでいる場合
else:
  if c < a < b: print("Yes")
  else: print("No")

"""
B問題_Cut.0
"""

x = list(input())

while x[-1] == "0":
  x.pop()

if x[-1] == ".":
  x.pop()
print("".join(x))

