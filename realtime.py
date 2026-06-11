# x = int(input())
# a = list(map(int, input().split()))
# values = [50, 10, 5, 1]
# ans = 0
# for i in range(4):
#   use = min(a[i], x // values[i])
#   ans += use
#   x -= values[i] * use
# print(ans)

# n = int(input())
# count = 0
# while n > 0:
#   count += 1
#   if n % 3 == 0: n //= 3
#   else: n -= 1
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
# prev = a[0]
# ans = 0
# for i in range(1, n):
#   if a[i] < prev:
#     ans += prev - a[i]
#   prev = max(prev, a[i])
# print(ans)

# n = int(input())
# a = set(map(int, input().split()))
# ret = 0
# while len(a) > 0:
#   ret += 1
#   min_val = min(a)
#   a = set(a_i for a_i in a if a_i % min_val != 0)
# print(ret)

"""
タイルの敷き詰め
1 * N = 長方形の面積
＝1 * i
・縦の長さが１、横の長さが１の正方形
・縦の長さが１、横の長さが２の長方形
・縦の長さが１、横の長さが３の長方形

壁にタイルを敷き詰める方法は全部で何通りあるか？
dp[i] = タイルを壁の横幅iまでに埋めた数
"""

# n = int(input())
# dp = [0] * (n + 1)
# dp[0] = 1 # 1通りは必ず存在する
# for i in range(1, n + 1):
#   # タイルを横に並べる
#   if i - 1 >= 0:
#     dp[i] += dp[i - 1]
#   if i - 2 >= 0:
#     dp[i] += dp[i - 2]
#   if i - 3 >= 0:
#     dp[i] += dp[i - 3]
# print(dp[n])


"""
表と数値 (1)
左上のマス：(i - 1, j - 1)
真上のマス：(i - 1, j)
右上のマス：(i - 1, j + 1)

dp[i][j] = 左上のマス＋真上のマス＋右上のマスを集約した数
"""

# N = 4
# a = list(map(int, input().split()))
# dp = [[0] * N for _ in range(N)]
# dp[0] = a

# for i in range(1, N):
#   for j in range(N):
#     # 真上のマスを集約して足す
#     dp[i][j] += dp[i - 1][j]
#     # 左上のマスを集約して足す
#     if j - 1 >= 0:
#       dp[i][j] += dp[i - 1][j - 1]
#     # 右上のマスを集約して足す
#     if j + 1 < N:
#       dp[i][j] += dp[i - 1][j + 1]
# print(dp[N - 1][N - 1]) # 右下のマスを求める

"""
表と数値 (2)
dp[i][j] = 左上のマス＋真上のマス＋右上のマスを集約した数
"""

# n = int(input())
# a = list(map(int, input().split()))
# dp = [[0] * n for _ in range(n)]
# dp[0] = a

# for i in range(1, n):
#   for j in range(n):
#     dp[i][j] += dp[i - 1][j]
#     if j - 1 >= 0:
#       dp[i][j] += dp[i - 1][j - 1]
#     if j + 1 < n:
#       dp[i][j] += dp[i - 1][j + 1]
#     dp[i][j] %= 100
# print(dp[n - 1][n - 1])


"""
3 つの仕事（難しい）
dp[i][j] = i日目に仕事jをした時の最大報酬
３種類の仕事：
仕事０：仕事１＋仕事２
仕事１：仕事０＋仕事２
仕事２：仕事０＋仕事１

０日目はどの仕事からも取り組める＝初めは全ての仕事を選べる
N日間でもらえる最大報酬はいくらか？
"""

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * 3 for _ in range(n)]

# # はじめは全ての仕事を選べる
# for j in range(3):
#   dp[0][j] = a[0][j]

# # 仕事０日目以降
# for i in range(1, n):
#   dp[i][0] += max(dp[i - 1][1], dp[i - 1][2]) + a[i][0]
#   dp[i][1] += max(dp[i - 1][0], dp[i - 1][2]) + a[i][1]
#   dp[i][2] += max(dp[i - 1][0], dp[i - 1][1]) + a[i][2]
# print(max(dp[n - 1]))

"""
コマの道順
"""

# n = int(input())
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = 1 # マスは必ず1通り存在する

# for i in range(n):
#   for j in range(n):
#     # 上から来るマスを集約
#     if i - 1 >= 0:
#       dp[i][j] += dp[i - 1][j]
#     # 左から来るマスを集約
#     if j - 1 >= 0:
#       dp[i][j] += dp[i][j - 1]
# print(dp[n - 1][n - 1])

"""
コマの道順 (壁あり)
"""

# n = int(input())
# s = [input() for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = 1

# for i in range(n):
#   for j in range(n):
#     if s[i][j] == "#":
#       continue
#     if i - 1 >= 0:
#       dp[i][j] += dp[i - 1][j]
#     if j - 1 >= 0:
#       dp[i][j] += dp[i][j - 1]
# print(dp[n - 1][n - 1])

"""
コマの道順 (重み付き)
"""

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# dp[0][0] = a[0][0]

# for i in range(n):
#   for j in range(n):
#     if i == 0 and j == 0:
#       continue
#     val = -10 ** 18
#     # 上から来るマスを集約して足す
#     if i - 1 >= 0:
#       val = max(val, dp[i - 1][j])
#     # 左から来るマスを集約して足す
#     if j - 1 >= 0:
#       val = max(val, dp[i][j - 1])
#     dp[i][j] += val + a[i][j]
# print(dp[n - 1][n - 1])

"""
コマの道順 (右上から)
dp[i][j] = マス(i, j)いへ移動する最小コスト
＝min(右から来るマス＋上から来るマス) + 現在いるマス
"""

# INF = 10**18
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# dp = [[INF] * n for _ in range(n)]
# dp[0][n - 1] = a[0][n - 1] # 右上のマスを設定

# for i in range(n):
#   for j in range(n - 1, -1, -1):
#     # 上からのマスを集約して足す
#     if i - 1 >= 0:
#       dp[i][j] = min(dp[i][j], dp[i - 1][j] + a[i][j])
#     # 右からのマスを集約して足す
#     if j + 1 < n:
#       dp[i][j] = min(dp[i][j], dp[i][j + 1] + a[i][j])
# print(dp[n - 1][0])


"""
数値の列
フィボナッチ数列
f(n) = f(n - 1) + f(n - 2)
"""

# n,x,y = map(int, input().split())
# for _ in range(n - 2):
#   x, y = y % 100, (x + y) % 100
# print(y)


"""
マスの移動 (1)
dp[i] = マスiに辿り着くまでの最小コスト

マスi - 1からAi秒かけて移動
マスi - 2から2Ai秒かけて移動
"""

# n = int(input())
# a = list(map(int, input().split()))
# dp = [0] * n
# dp[1] = a[1]
# for i in range(2, n):
#   dp[i] += min(dp[i - 1] + a[i], dp[i - 2] + 2*a[i])
# print(dp[n - 1])

"""
マスの移動 (2)
dp[i] = マスiに到達するまでの最小コスト
"""

# INF = 10**18
# N,M = map(int, input().split())
# a = list(map(int, input().split()))
# dp = [INF] * N

# dp[0] = 0 # マス0から開始
# for i in range(1, N):
#   for m in range(1, M + 1):
#     # マスが存在する範囲か
#     if i - m >= 0:
#       dp[i] = min(dp[i], dp[i - m] + m*a[i])
# print(dp[N - 1])

"""
すごろく
到達可能性（部分和問題）
"""

# n,m = map(int, input().split())
# d = list(map(int ,input().split()))
# dp = [False] * (n + 1)
# dp[0] = True # マス0から開始

# for i in range(n + 1):
#   for j in range(m):
#     if i - d[j] >= 0 and dp[i - d[j]]:
#       dp[i] = True
#       break
# print("Yes" if dp[n] else "No")

"""
階段の登り方
"""

# n = int(input())
# dp = [0] * (n + 1)
# dp[0], dp[1] = 1, 1

# for i in range(2, n + 1):
#   dp[i] = dp[i - 1] + dp[i - 2]
# print(dp[n])

"""
部分和問題のDP
N個の整数の中からいくつかを選んでXを作ることはできるか？

dp[j] = 「これまで見た要素の中からいくつか選んで、jを作れるか」
"""

# import sys
# sys.setrecursionlimit(10**6)

# # 先頭から i 個の要素を使って、合計 j を作れるか？
# # メモ化再帰
# def func(i ,j) -> int:
#   # 過去に計算済みの場合メモに記録された値を返す
#   if memo[i][j] != -1: return memo[i][j]
  
#   if i == 0:
#     memo[i][j] = j == 0
#   else:
#     memo[i][j] = 0
#     if j >= a[i - 1] and func(i - 1, j - a[i - 1]) == 1:
#       memo[i][j] = 1
#     if func(i - 1, j) == 1:
#       memo[i][j] = 1
#   return memo[i][j]

# n,x = map(int, input().split())
# a = list(map(int, input().split()))
# # func(i, j) の値を記録するメモ(配列)を用意する
# # -1 なら未記録、0 なら false、1 なら true
# memo = [[-1] * (x + 1) for _ in range(n + 1)]
# print("Yes" if func(n, x) == 1 else "No")

# DFS解法
# def dfs(l, path):
#   if len(path) == N:
#     print(*path)
#     return
#   for i in range(l, R+1):
#     path.append(i)
#     dfs(i, path)
#     path.pop()

# N, L, R = map(int, input().split())
# dfs(L, [])

"""
頂点を塗る

色が塗られる＝訪問ずみ
色が塗られていない＝未訪問
-1：未訪問/ -1以外：訪問済み

k回頂点の色塗る。
k回の操作によって色が塗られた頂点を番号が小さい順にN行で出力
"""
# N,M = map(int, input().split())
# G = [[] for _ in range(N)] # 隣接リストを作成[[]]（単純無向グラフ）
# dist = [-1] * N # 何手目で頂点を訪れたかを管理する配列
# for _ in range(M):
#     A,B = map(int, input().split())
#     G[A].append(B) # 頂点Aに頂点Bの辺を張る
#     G[B].append(A) # 頂点Bに頂点Aの辺を張る

# from collections import deque

# # BFS開始
# todo = deque([0])  # 頂点の訪問を管理するtodoリスト
# dist[0] = 0 # 頂点0に0手目で訪問できる
# nodes = [[] for _ in range(N)] # 色を塗った頂点番号を管理する配列
# nodes[0].append(0)
# # 未訪問の頂点がなくなるまで繰り返す
# while todo:
#     v = todo.popleft()
#     for nv in G[v]:
#         if dist[nv] != -1:
#             continue
#         dist[nv] = dist[v] + 1 # 頂点nvには距離v＋１で到達できる
#         nodes[dist[nv]].append(nv) # nv手目で訪れた頂点番号を記録
#         todo.append(nv) # 次に訪問する頂点を追加

# for k in range(N):
#     nodes[k].sort()
#     print(*nodes[k])

"""
行きがけ順
(https://algo-method.com/tasks/525)
"""
# import sys
# sys.setrecursionlimit(10**6)
# N = int(input()) # 頂点数の入力
# P = list(map(int, input().split())) # 親頂点リスト

# # 各頂点の子頂点リストを作る
# chs = [[] for _ in range(N)]
# for v in range(1, N):
#     # 頂点 v の親
#     p = P[v - 1]
#     # 親 p の子頂点リストに頂点 v を挿入
#     chs[p].append(v)

# # 頂点 v を根とする部分木を探索
# def rec(v, chs):
#     print(v, end=" ")
#     # 頂点 v の各子頂点を探索
#     for ch in chs[v]:
#         # 子頂点 ch を根とした部分木を再帰的に探索
#         rec(ch, chs)

# rec(0, chs)

"""
部分和問題への導入
(https://algo-method.com/tasks/336)

合計jを作れる／作れない
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split()))
# dp = [[False] *  M for _ in range(N)]
# dp[0][0] = True

# for i in range(N - 1):
#     for j in range(M):
#         if not dp[i][j]:
#             continue
#         # 選ばない
#         dp[i + 1][j] = True
#         # 選ぶ
#         if j + A[i] < M:
#             dp[i + 1][j + A[i]] = True

# print(sum(dp[N - 1]))


"""
部分和問題
(https://algo-method.com/tasks/337)

合計jを作れる／作れない
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# # iごとの合計jを管理する配列
# dp = [[False] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = True

# for i in range(N):
#     for j in range(M + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True
        
#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = True
# print("Yes" if dp[N][M] else "No")


"""
部分和問題 (最小個数)
(https://algo-method.com/tasks/350)

合計jの最小個数
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# INF = 10**8
# dp = [[INF] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     for j in range(M + 1):
#         if dp[i][j] == INF:
#             continue
#         # 選ばない（前の状態を引き継ぐ）
#         dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
#         # 選ぶ（前の状態を加算）
#         if j + W[i] <= M:
#             # +1で1個ボールを加算
#             dp[i + 1][j + W[i]] = min(dp[i + 1][j + W[i]], dp[i][j] + 1)

# print(dp[N][M] if dp[N][M] != INF else -1)

"""
部分和問題 (数え上げ)
(https://algo-method.com/tasks/310)

通り数を持つ
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split()))
# MOD = 1000
# dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 1

# for i in range(N):
#     for j in range(M + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] += dp[i][j]
#         dp[i + 1][j] %= MOD

#         if j + A[i] <= M:
#             dp[i + 1][j + A[i]] += dp[i][j]
#             dp[i + 1][j + A[i]] %= MOD
# print(dp[N][M])


"""
部分和問題の応用 (1)
(https://algo-method.com/tasks/352)

全体和＝S
S % A = B   

選ぶ／選ばない

余りを持つ
dp[i][r] = 先頭から i 個見た時、余り rが作れるか。
"""

# N,A,B = map(int, input().split())
# X = list(map(int, input().split()))
# dp = [[False] * A for _ in range(N + 1)]
# dp[0][0] = True

# for i in range(N):
#     for j in range(A):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True
#         r = (j + X[i]) % A
#         dp[i + 1][r] = True

# print("Yes" if dp[N][B] else "No")

"""
部分和問題の応用 (2)
(https://algo-method.com/tasks/353)

2つの箱に入っているホールの重さの総和の差がいくつになるか。
→重さの総和のさをできるだけ小さくする
片方の合計jだけ持つ
片方の合計が決まれば、自動的にもう片方の値も決まる

全体和(ボールの重さの集計）＝S

グループA:j
グループB：S - j
全体和＝j＋（S-j)
総和の差＝｜jー（S-j）｜
"""

# N = int(input())
# W = list(map(int, input().split()))
# S = sum(W)
# dp = [[False] * (S + 1) for _ in range(N + 1)]
# dp[0][0] = True # 何も選ばない場合は合計０

# for i in range(N):
#     for j in range(S + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True
#         dp[i + 1][j + W[i]] = True

# ans = S
# # 総和の差を求める
# for j in range(S + 1):
#     if dp[N][j]:
#         ans = min(ans, abs(j - (S - j)))
# print(ans)

"""
ナップサック問題への導入
(https://algo-method.com/tasks/341)

合計 j を作る時の最大価値

dp[i][j] = 現在の価値
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# dp = [[-1] * M for _ in range(N)]
# dp[0][0] = 0

# for i in range(N - 1):
#     for j in range(M):
#         if dp[i][j] == -1:
#             continue
#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

#         if j + A[i] < M:
#             dp[i + 1][j + A[i]] = max(
#                 dp[i + 1][j + A[i]],
#                 B[i] + dp[i][j]
#             )
# print(dp[N - 1][M - 1])

"""
ナップサック問題
(https://algo-method.com/tasks/342)

合計 j を作る時の最大価値
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# V = list(map(int, input().split()))
# dp = [[-1] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     for j in range(M + 1):
#         if dp[i][j] == -1:
#             continue
#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = max(
#                 dp[i + 1][j + W[i]],
#                 V[i] + dp[i][j]
#             )
# print(max(dp[N]))

"""
マス目の経路最適化
(https://algo-method.com/tasks/856)

直前の行を持つ
差＝直前の行ー次の行
上中下の3方向に遷移

列を軸に考える
"""

# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# P = [A, B, C]

# INF = 10**8
# dp = [[INF] * 3 for _ in range(N)]

# # 0行目を初期化
# for j in range(3):
#     dp[0][j] = 0

# for i in range(N - 1):

#     for now in range(3):

#         for next in range(3):
#             cost = abs(P[now][i] - P[next][i + 1])
#             dp[i + 1][next] = min(
#                 dp[i + 1][next],
#                 dp[i][now] + cost
#             )
# print(min(dp[N - 1]))

"""
部分和問題への導入
(https://algo-method.com/tasks/336)

先頭から i 個見た時、合計 j を作れるかを
状態に持つ。

＝部分和の集合を求める
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split()))
# dp = [[False] * M for _ in range(N)]
# dp[0][0] = True

# for i in range(N - 1):
#     for j in range(M):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True
        
#         if j + A[i] < M:
#             dp[i + 1][j + A[i]] = True
# print(sum(dp[N - 1]))

"""
部分和問題
(https://algo-method.com/tasks/337)
dp[i][j] = 先頭からi個見た時、合計jを作れるかの部分和の集合として考える

合計がMとなるようなボールの入れ方が存在するか
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# dp = [[False] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = True

# for i in range(N):
#     for j in range(M + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True

#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = True

# print("Yes" if dp[N][M] else "No")

"""
部分和問題（最小個数）
(https://algo-method.com/tasks/350)
最小個数を状態に持つ
直前の状態＝dp[i][j]
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# INF = 10**8
# dp = [[INF] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     for j in range(M + 1):
#         if dp[i][j] == INF:
#             continue
#         dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = min(
#                 dp[i + 1][j + W[i]],
#                 dp[i][j] + 1 # ボールの数を加算
#             )
# print(dp[N][M] if dp[N][M] != INF else -1)


"""
部分和問題 (数え上げ)
(https://algo-method.com/tasks/310)

いくつかの整数を選ぶ方法（＝選ぶ／選ばないの２択）
通り数を持つ
直前に選んだ個数＝dp[i][j]
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split()))
# MOD = 1000

# dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 1

# for i in range(N):
#     for j in range(M + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] += dp[i][j]
#         dp[i + 1][j] %= MOD
        
#         if j + A[i] <= M:
#             dp[i + 1][j + A[i]] += dp[i][j]
#             dp[i + 1][j + A[i]] %= MOD
# print(dp[N][M])

"""
部分和問題の応用 (1)
(https://algo-method.com/tasks/352)

余りを状態に持つ（状態圧縮）
"""

# N,A,B = map(int, input().split())
# X = list(map(int, input().split()))
# dp = [[False] * A for _ in range(N + 1)]
# dp[0][0] = True

# for i in range(N):
#     for j in range(A):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True
#         r = (j + X[i]) % A
#         dp[i + 1][r] = True

# print("Yes" if dp[N][B] else "No")


"""
部分和問題の応用 (2)
(https://algo-method.com/tasks/353)

２つの箱とN個のボール
片方の値が確定すれば、もう片方も自動的に決まる

片方のグループの部分和の合計を持つ

箱A：j
箱B：Sum - j
合計＝j + (Sum - j)

２つの総和の差＝j - (Sum - j)
"""

# N = int(input())
# W = list(map(int, input().split()))
# S = sum(W)

# dp = [[False] * (S + 1) for _ in range(N + 1)]

# dp[0][0] = True

# for i in range(N):
#     for j in range(S + 1):
#         if not dp[i][j]:
#             continue
#         dp[i + 1][j] = True

#         if j + W[i] <= S:
#             dp[i + 1][j + W[i]] = True


# ans = S
# # 箱A,Bの総和の最小値の差を求める
# for j in range(S + 1):
#     if dp[N][j]:
#         ans = min(ans, abs(j - (S - j)))

# print(ans)




"""
ナップサック問題への導入
(https://algo-method.com/tasks/341)

合計 j を作る時の最大ポイントを持つ
右下マスに辿り着くための最適スコアの最大値を更新していく。
"""

# N,M = map(int, input().split())
# A = list(map(int, input().split())) # 移動
# B = list(map(int, input().split())) # ポイント

# dp = [[-1] * M for _ in range(N)]
# dp[0][0] = 0

# for i in range(N - 1):
#     for j in range(M):
#         if dp[i][j] == -1:
#             continue
        
#         # 選ばない（直前のポイントを引き継ぐ）
#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

#         # 選ぶ（現在の最大ポイントを更新）
#         if j + A[i] < M:
#             dp[i + 1][j + A[i]] = max(
#                 dp[i + 1][j + A[i]],
#                 dp[i][j] + B[i]
#             )
# print(dp[N - 1][M - 1])


"""
ナップサック問題
(https://algo-method.com/tasks/342)

重さ j を作る時の最大価値を持つ
""" 

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# V = list(map(int, input().split()))

# dp = [[-1] * (M + 1) for _ in range(N + 1)]
# dp[0][0] = 0

# for i in range(N):
#     for j in range(M + 1):
#         if dp[i][j] == -1:
#             continue

#         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

#         if j + W[i] <= M:
#             dp[i + 1][j + W[i]] = max(
#                 dp[i + 1][j + W[i]],
#                 dp[i][j] + V[i]
#             )

# print(max(dp[N]))


"""
マス目の経路最適化（難しい）
(https://algo-method.com/tasks/856)

直前の列で選んだ最小コスト

部分和問題（選ぶ・選ばない）ではない
"""

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# P = [A, B, C] # 3N(i, j)
# INF = 10**8
# dp = [[INF] * 3 for _ in range(N)] # N*3(j, i)

# # 初期条件
# for r in range(3):
#     dp[0][r] = 0

# for i in range(N - 1):
#     # 現在列を移動
#     for now in range(3):
#         # 次の列へ移動
#         for next in range(3):
#             # 直前の列で選んだコストを計算
#             cost = abs(P[now][i] - P[next][i + 1])
            
#             dp[i + 1][next] = min(
#                 dp[i + 1][next],
#                 dp[i][now] + cost
#             )
# print(min(dp[N - 1]))


"""
部分和問題 (K 個以内)
(https://algo-method.com/tasks/312)

jを作れる最小個数（１次元）
"""

# N,M,K = map(int, input().split())
# A = list(map(int, input().split()))
# INF = 10**8
# dp = [INF] * (M + 1)
# dp[0] = 0

# for i in range(N):
#     # 同じ数字（添え字）を複数回使わないために逆順で走査
#     for j in range(M, -1, -1):
#         if dp[j] == INF:
#             continue

#         if j + A[i] <= M:
#             dp[j + A[i]] = min(
#                 dp[j + A[i]],
#                 dp[j] + 1
#             )

# print("Yes" if dp[M] <= K else "No")


"""
もう一つのナップサック問題
(https://algo-method.com/tasks/7147e09c64ad8783)

価値 j で作れる最大の重さ（❌）
価値 v を作れる最小の重さ（⭕️）

重さ（M）ではなく、価値（V）を基準に考える。
"""

# N,M = map(int, input().split())
# W = list(map(int, input().split()))
# V = list(map(int, input().split()))
# INF = 10**9

# S = sum(V)
# dp = [INF] * (S + 1)
# dp[0] = 0

# for i in range(N):
#     for v in range(S, -1, -1):
#         if dp[v] == INF:
#             continue
    
#         dp[v + V[i]] = min(
#             dp[v + V[i]],
#             dp[v] + W[i]
#         )

# ans = 0
# for v in range(S + 1):
#     if dp[v] <= M:
#         ans = max(ans, v)
# print(ans)


"""
マス目の経路最適化 (2)
(https://algo-method.com/tasks/2925Drvr)

直前の列の塗り方を持たせる
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**9
dp = [[INF] * 4 for _ in range(N)]

dp[0][1] = A[0] # 上だけ黒 
dp[0][2] = B[0] # 下だけ黒
dp[0][3] = A[0] + B[0] # 上下黒

for i in range(1, N):
    dp[i][1] = min(dp[i - 1][1], dp[i - 1][3]) + A[i]
    dp[i][2] = min(dp[i - 1][2], dp[i - 1][3]) + B[i]
    dp[i][3] = min(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + A[i] + B[i]

print(min(dp[N  -1]))
    
