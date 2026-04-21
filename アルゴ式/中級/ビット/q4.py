"""
フラグ状態の復元 (2)
(https://algo-method.com/tasks/1706y0fU)
"""

n = int(input())
x = 0
ans = []
for i in range(30):
  if n & (1 << i):
    x += 1
    ans.append(i)
print(x)
print(*ans)