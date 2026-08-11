"""
まとめ売り（計算量）
"""

# N = int(input()) # カードの枚数
# C = list(map(int, input().split())) # カードiの在庫数
# Q = int(input())
# even_lst = [i for i in range(N) if i % 2 == 0]
# count = len(even_lst)

# # 愚直の解法
# total = 0
# for i in range(Q):
#     query = list(map(int, input().split()))
#     # 単品販売：
#     if query[0] == 1:
#        x = query[1] - 1
#        a = query[2]
#        if a <= C[x]:
#            C[x] -= a
#            total += a
#     # 奇数セット販売
#     elif query[0] == 2:
#         a = query[1]
#         # 奇数のカード番号を全て走査するため無駄
#         if all(a <= C[i] for i in even_lst):
#             total += (a * count)

#             for i in even_lst:
#                 C[i] -= a
#     # 全種類販売
#     else:
#         a = query[1]
#         if all(a <= C[i] for i in range(N)):
#             total += (a * N)
            
#             for i in range(N):
#                 C[i] -= a
# print(total)


"""
幅優先探索

ゴールまでの最小移動回数を求める
始点からの距離が小さい点から順番に探索
"""

# from collections import deque

# R,C = map(int, input().split()) # R:行数、C:列数
# sy,sx = map(int, input().split()) # 始点の座標
# gy,gx = map(int, input().split()) # 終点の座標
# s = [input() for _ in range(R)] # 盤面の文字列

# dist = [[-1] * C for _ in range(R)] # 盤面ごとの移動手数を記録する配列
# sy -= 1; sx -= 1
# gy -= 1; gx -= 1

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# que = deque() # 始点を設定
# que.append([sy, sx])
# dist[sy][sx] = 0

# while que:
#     si,sj = que.popleft()
    
#     # 上下左右の移動
#     for dy, dx in d:
#         y = si + dy
#         x = sj + dx
#         # マスが壁かすでに訪問済みの場合は何もしない
#         if s[y][x] == "#" or dist[y][x] != -1:
#             continue
#         # 現在のマスから次のマスへの移動手数を記録
#         dist[y][x] = dist[si][sj] + 1
#         # キューの更新
#         que.append([y, x])

# print(dist[gy][gx])


"""
深さ優先探索
行き止まりになるまで探索

魚屋に辿り着けるかどうかを求める
＝到達可能性のみ考えればいい
"""

# import sys
# sys.setrecursionlimit(10**9)

# H,W = map(int, input().split())
# S = [input() for _ in range(H)]
# sy,sx = 0,0 # 始点
# gy,gx = 0,0 # 終点

# # 始点、終点の座標を確定させる
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == 's':
#             sy, sx = i, j
#         if S[i][j] == 'g':
#             gy, gx = i, j

# visited = [[False] * W for _ in range(H)] # 座標Si,jに到達できるかを管理する配列
# visited[sy][sx] = True # 始点はすでに訪問済み

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4近傍

# def dfs(y: int, x: int):
#     visited[y][x] = True

#     for dy, dx in d:
#         di = y + dy
#         dj = x + dx

#         if not(0 <= di < H and 0 <= dj < W):
#             continue
        
#         if S[di][dj] == "#":
#             continue
        
#         # 未訪問の場合のみ次のマスへ訪問する
#         if not visited[di][dj]:
#             dfs(di, dj)

# # 始点から呼び出す
# dfs(sy, sx)
# print("Yes" if visited[gy][gx] else "No")


"""
Frog1
動的計画法

状態遷移
dp[i] = 足場 1 から足場 i へ移動するときの最小コスト

足場1から足場1に移動するための最小コストは？
足場1から足場2に移動するための最小コストは？
足場1から足場3に移動するための最小コストは？
"""

# N = int(input())
# h = list(map(int, input().split()))
# dp = [0] * N
# dp[0] = 0 # 足場1→1への移動コストは0
# # 2つ目の足場はジャンプ元が１通り
# dp[1] = dp[0] + abs(h[0] - h[1])

# # それ以降の足場はジャンプ元が２通りあるため、コストが小さい方を採用する
# for i in range(2, N):
#     dp[i] = min(
#        dp[i - 1] + abs(h[i - 2] - h[i - 1]),
#        dp[i - 2] + abs(h[i - 2] - h[i])
#     )
# print(dp[N - 1])


"""
ナップサック問題（動的計画法）
部分和問題：選ぶ／選ばない

品物の価値の総和の最大値（MAX）
dp[i][w] = 重さ i の時、合計 j が作れる時の、価値の合計の最大値

O(NW)
"""

# N,W = map(int, input().split())
# dp = [[0] * (W + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(1, N + 1):
#     w, v = map(int, input().split())
    
#     for j in range(W + 1):
#         # 品物 i を使わない場合
#         dp[i][j] = max(dp[i][j], dp[i - 1][j])

#         # 品物 i を使う場合
#         if j + w <= W:
#             dp[i][j] = max(
#                 dp[i][j],
#                 dp[i - 1][j + w] + v
#             )
# # dp[N]の中で一番価値の合計が高いものが答え
# print(max(dp[N]))

"""
コンテスト（動的計画法）
部分和問題

dp[i][s] = 先頭から i 個選んだ時、合計 jが作れるか
＝和をちょうどにできるか？

O(NP)
"""

# N = int(input())
# p = list(map(int, input().split()))
# S = sum(p)
# dp = [[False] * (S + 1) for _ in range(N + 1)]
# dp[0][0] = True

# for i in range(N):
#     for j in range(S + 1):
#         if not dp[i][j]:
#             continue

#         dp[i + 1][j] = True

#         if j + p[i] <= S:
#             dp[i + 1][j + p[i]] = True
# print(sum(dp[N]))

"""
集合
A = {1,2,3,4,5}
B = {3,4,5}

空集合：{}
＝要素が何もない集合

和集合（OR）：A ∪ B = {1,2,3,4,5}
＝2つの集合A,BについてAまたはBの少なくとも一方に含まれる要素を集めた集合
A | B

積集合（AND）：A ∩ B = {3,4,5}
＝2つの集合A,Bについて、AとBの両方に含まれる要素を集めた集合（A,Bの共通部分）
A & B

2^N通り考えられる
部分集合：A ⊂ B
＝集合Aの要素がすべて集合Bに含まれている時

部分集合：B ⊂ A
＝集合Bの要素がすべて集合Aに含まれている時

全体集合：すべての集合からなる要素（U）

補集合（XOR：0,1の反転）；全体集合Uに含まれていて、集合Aに含まれていない集合
例）U＝{0,1,2,3,4,5,6} 補集合；A = {6}
"""

"""
組み分け（集合）
N人の社員を３つ以下のグループに最適に分割するプログラム
グループ分けの好ましさの最大値を求める

集合に対する全探索を行う問題
"""

N = int(input())
A = []

for i in range(N - 1):
    lst = list(map(int, input().split()))
    A.append([0] * (i + 1) + lst)

# 集合としてありうるものの個数
ALL = 1 << N # 2^N - 1通り

# happy[n]：nで表現される集合をグループにしたときの幸福度
happy = [0] * ALL 

# nで表現される集合に要素 i が含まれるかを判定する関数
def has_bit(n, i):
    return n & (1 << i)

# happyの値を前もって計算
for n in range(ALL):
    for i in range(N): # 社員番号（0〜N-1）
        for j in range(i + 1, N): # 社員番号（1〜N-1）
            # 集合nに要素 i が含まれるか
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]
                print(f"集合：{n} 要素i：{i} 要素j：{j}")

ans = -1

# ３つのグループに分ける
for n1 in range(ALL):
    for n2 in range(ALL):
        # n1とn2が重複があれば無視
        if n1 & n2 > 0:
            continue
        n3 = ALL - 1 - (n1 | n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans) 



