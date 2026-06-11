"""
部分和問題
(https://algo-method.com/tasks/337)
到達できる／できないの状態を持つ

※bit全探索でも解ける。
選ぶ／選ばないの２通り＝O(2^N)通り
でも、N <=100で計算量が爆発する。
そのため、O(NM）のDPで解く。
dp[i][j]は1回管理すればいい
"""

N,M = map(int ,input().split())
W = list(map(int, input().split()))
# i個番目時点で合計jの重さを作れるかを管理する配列
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for j in range(M + 1): # 合計値の範囲
        if not dp[i][j]:
            continue
        # ボールを選ばない：重さ変化なし
        dp[i + 1][j] = True
        
        # ボールを選ぶ：重さが変化あり
        if j + W[i] <= M:
            dp[i + 1][j + W[i]] = True
if dp[N][M]:
    print("Yes")
else:
    print("No")




