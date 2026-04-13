"""
メモ化のメリット (2)
(https://algo-method.com/tasks/2e0d7baa2b3918d6)
"""

memo = {}
counter = [0] * 11

def rec(n):
  counter[n] += 1
  if n in memo:
    return memo[n]
  if n in (1, 2):
    return 1
  
  memo[n] = rec(n - 2) + rec(n - 1)
  return memo[n]

result = rec(10)
for idx in range(1, 11):
  print(counter[idx])