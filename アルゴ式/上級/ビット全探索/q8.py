"""
部分和問題
(https://algo-method.com/tasks/1131I9eL)
ビット全探索
"""

n,v = map(int, input().split())
a = list(map(int, input().split())) + [0]
for S in range(1 << n):
    total = 0
    for j in range(n):
        if S & (1 << j):
            total += a[j]
    if total == v:
        print("Yes")
        exit()
print("No")

# 別解（動的計画法）
n,v = map(int, input().split())
a = list(map(int, input().split())) + [0]
dp = [[False] * (v + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1): # N個の整数
  for j in range(v + 1): # 総和V
    if dp[i - 1][j]:
      dp[i][j] = True
    if j >= a[i] and dp[i - 1][j - a[i]]:
      dp[i][j] = True
    
print("Yes" if dp[n][v] else "No")