"""
B問題_326-like Numbers

百の位：n / 100
十の位：(n % 100) / 10
一の位：n % 10
"""

n = input()
a,b,c = map(int, n)
while a * b != c:
  k = str(a*100 + 10*b + c + 1)
  a,b,c = map(int, k)
print(a*100 + b*10 + c)
