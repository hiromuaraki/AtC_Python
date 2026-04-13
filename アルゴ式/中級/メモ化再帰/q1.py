"""
メモ化のメリット (1)
(https://algo-method.com/tasks/5f674b32c7d3ca93)
メモ化なし
nが何回呼ばれたかを出力するプログラム
"""
x = 10
counter = [0] * (x + 1)

def rec(n):
  counter[n] += 1
  if n in (1, 2):
    return 1
  else:
    return rec(n - 2) + rec(n - 1)

result = rec(x)
for idx in range(1, x + 1):
  print(counter[idx])