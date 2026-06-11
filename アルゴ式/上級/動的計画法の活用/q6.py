"""
部分和問題の応用 (2)
(https://algo-method.com/tasks/353)

片方の合計のみ持つ
＝片方の合計が決まれば、もう片方も自動的に決まる

全体和＝S
グループA：j
グループB：S - j

S＝グループA＋グループB
グループB ＝S-グループA

2つのグループの差
＝j - (S - j)

"""

N = int(input())
W = list(map(int ,input().split()))
S = sum(W) # 全体和

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True # 先頭から i 個見た時、合計 j を作れるか。

for i in range(N):
    for j in range(S + 1):
        if not dp[i][j]:
            continue
        # 選ばない
        dp[i + 1][j] = True
        # dp[i][j]＝今まで見た要素で作れる部分和
        # jは今ままでの部分和、そこへW[i]足しても全要素合計＝Sの範囲内のため
        # 理論上不要だが 可読性と安全のため条件を書いている。
        if j + W[i] <= S:
            dp[i + 1][j + W[i]] = True

ans = S
# グループA、Bの総和の差を求める
for j in range(S + 1):
    if dp[N][j]:
        ans = min(ans, abs(j - (S - j)))
print(ans)