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

n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])