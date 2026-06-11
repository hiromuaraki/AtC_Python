"""
部分和問題の応用 (1)
(https://algo-method.com/tasks/352)
余りを持つ
先頭i個見た時、余りrを作れるか
"""

N,A,B = map(int, input().split())
X = list(map(int, input().split()))
dp = [[False] * A for _ in range(N + 1)]
dp[0][0] = True  # 何も選ばず余り０は作れる

for i in range(N):
    for j in range(A):
        if not dp[i][j]:
            continue
        dp[i + 1][j] = True
        r = (j + X[i]) % A
        dp[i + 1][r] = True

print("Yes" if dp[N][B] else "No")