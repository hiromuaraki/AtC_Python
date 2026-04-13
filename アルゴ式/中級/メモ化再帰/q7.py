"""
トリボナッチ数列
(https://algo-method.com/tasks/63d1a87706a63320)
"""

MOD = 10**6
n = int(input())
dp = [0] * max(3, n + 1)

dp[0],dp[1],dp[2] = 1, 1, 1
for i in range(3, n + 1):
  dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
print(dp[n])

a,b,c = 1,1,1
for _ in range(3, n + 1):
  a,b,c = b,c,(a + b + c) % MOD

print(c)