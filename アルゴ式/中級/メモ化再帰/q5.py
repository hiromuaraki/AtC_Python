"""
部分和問題
(https://algo-method.com/tasks/427)
"""

n,x = map(int, input().split())
a = list(map(int, input().split()))

# 再帰関数 (A の前から i 個の中からいくつか選んで j を作れるか)
def f(i, j) -> bool:
  if i == 0: return j == 0
  
  flag = False
  if j >= a[i - 1] and f(i - 1, j - a[i - 1]):
    flag = True
  if f(i - 1, j):
    flag = True

  return flag
print("Yes" if f(n, x) else "No")