"""
数値の列
(https://algo-method.com/tasks/302)

状態遷移の設計
・f(n) = f(n - 1) + f(n - 2)
・x,y = y,(x + y) % 100

フィボナッチ数列

"""

n,x,y = map(int, input().split())

for _ in range(n - 1):
  x,y = y,(x + y) % 100
print(x)

# 別解（漸化式ver）
fib = [0] * n
fib[0], fib[1] = x, y
for i in range(2, n):
  fib[i] = (fib[i - 2] + fib[i - 1]) % 100
print(fib[n - 1])
  
  