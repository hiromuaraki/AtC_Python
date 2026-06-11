"""
部分和問題への導入
(https://algo-method.com/tasks/336)

コマが最下段にたどりついたとき、移動先として考えられるマスはいくつありますか。
dp[i][j] = i回目までの操作で合計jを作れるか？
の状態を保存する

行 i の意味：何個数字を処理したか
列 j の意味：現在の合計値

合計値が変化するのは j + A[i]の時（右のマスへの移動時のみ）＝列 j が変化する
＝右下移動
"""

N,M = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]にマスが存在しうるかを記録するテーブル配列
dp = [[False] *  M for _ in range(N)]

dp[0][0] = True # 初期状態（左上にマスがある）

for i in range(N - 1):
    for j in range(M):
        # その時点で合計 j を作れないなら何もしない
        if not dp[i][j]:
            continue
        # 行移動：マスを何も選ばない場合、合計値は常に0
        # 合計値の変化なし
        dp[i + 1][j] = True
        # 列移動：マスを選ぶ場合 合計値変化あり
        # i + 1個目の時点で合計 j + A[i]を作れるか
        if j + A[i] < M:
            dp[i + 1][j + A[i]] = True

print(sum(dp[N - 1]))