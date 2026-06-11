"""
残った数を K の倍数に
(https://algo-method.com/tasks/2929nKVo)

dp[i][r]=
先頭i文字を見て作れる部分列のうち、
余りrになるものが何個あるか

例）
4 3
1135

””  0
”1” 1
"1" 1
"3" 0
"5" 2
"11" 2
"13" 1
"15" 0
"13" 1
"15" 0
"35" 2
"113" 2
"115" 1
"135" 0
"135" 0
"1135" 1

"""
MOD = 10**9 + 7
N,K = map(int, input().split())
S = input()

dp = [[0] * K for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    # 先頭からi文字目を見る
    d = int(S[i])
    # rは余りの種類数
    for r in range(K):
        # 選ばない（状態を引き継ぐ）
        dp[i + 1][r] += dp[i][r]
        dp[i + 1][r] %= MOD

        # 余りの種類数ごとに振り分けるために計算
        nr = (r * 10 + d) % K
        # 選ぶ
        dp[i + 1][nr] += dp[i][r]
        dp[i + 1][nr] %= MOD

# N文字見終わったときの余りが0（＝Kの倍数）の個数
# ””（空文字）の含まれている個数を-1
print(dp[N][0] - 1)