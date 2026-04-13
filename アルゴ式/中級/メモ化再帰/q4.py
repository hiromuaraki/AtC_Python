"""
フィボナッチ数列のメモ化
(https://algo-method.com/tasks/423)
"""

n = int(input())
fib = [-1] * (n + 1)
fib[0], fib[1] = 0, 1

def func(x: int) -> int:
  print(f"func({x})を計算します。")
  if fib[x] != -1: return fib[x]
  fib[x] = func(x - 1) + func(x - 2)
  return fib[x]
print(func(n))
