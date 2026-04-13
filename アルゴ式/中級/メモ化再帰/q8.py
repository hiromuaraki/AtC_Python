"""
互除法
(https://algo-method.com/tasks/3f02d7819f034815)

最大公約数を求める：ユークリッドの互除法
"""
import sys
sys.setrecursionlimit(10**9)

def gcd(x: int, y: int) -> int:
  if y == 0: return x
  return gcd(y, x % y)

n,m = map(int, input().split())
print(gcd(n, m))