"""
B問題_3-smooth Numbers
(https://atcoder.jp/contests/abc324/tasks/abc324_b)
素因数分解の問題
"""

n = int(input())
while n % 2 == 0: n //= 2
while n % 3 == 0: n //= 3
if n >= 2:  print("No")
else: print("Yes")
