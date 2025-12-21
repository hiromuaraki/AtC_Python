"""
難しい
正しい場合分けと問題の読解ができない
m < xのときh時m分
m > xのときh+1問m分
"""

X,H,M = map(int, input().split())
if M < X:
  print(X - M)
else:
  print(60 + X - M)