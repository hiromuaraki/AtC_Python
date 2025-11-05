"""
C問題：解けた
"""

S = input()
print('+'*(len(S)+2))
print('+'+S+'+')
print('+'*(len(S)+2))


"""
B問題：解けた（グリッド）
座標を作成し改善

(x, y)の座標から上下左右に移動
上下左右の座標をデータで表現
"""

# リファクタリング後
N,H,W = map(int, input().split())
sy, sx  = map(int, input().split())
sy -= 1; sx -= 1 # 開始地点を0-indexedに調整
move = input()
grid = [list(input().split()) for _ in range(H)]
# 上下左右の座標
D = {"F": (-1, 0), "B": (1, 0), "L": (0, -1), "R": (0, 1)}
visited = set()

for t in move:
  dy, dx = D[t]
  sy, sx = dy + sy, dx + sx
  if 0 <= sy < H and 0 <= sx < W:
    # 1度訪れたマスは訪れない
    if (sy, sx) not in visited:
      print(grid[sy][sx])
      visited.add((sy, sx))


# 修正前コード
# for t in move:
#   # 左
#   if t == 'L' and  W-1 > 0 and grid[y][x-1] not in C:
#     print(grid[y][x-1])
#     C.add((y, x-1))
#     x -= 1
#   # 右
#   if t == 'R' and x < W-1 and grid[y][x+1] not in C:
#     print(grid[y][x+1])
#     C.add((y, x+1))
#     x += 1
#   # 前
#   if t == 'F' and y > 0 and grid[y-1][x] not in C:
#     print(grid[y-1][x])
#     C.add((y-1, x))
#     y -= 1
#   # 後ろ
#   if t == 'B' and y < H-1 and grid[y+1][x] not in C:
#     print(grid[y+1][x])
#     C.add((y+1, x))
#     y += 1


"""
C問題_部分和問題（bit全探索）
若干難しい
選ぶ／選ばない
計算量：2^N通り
計算量：O(N*2^N）
カードの枚数 N枚
2^N（指数関数）に回増えていく

2^N-1回ループ
P66に記載
1.2進法を利用して選び方に番号を振る
2.選び方の番号を全探索

"""

N, S = map(int, input().split())
A = list(map(int, input().split()))

# ビット演算を使う
for bit in range(1 << N): # 2^N通り試す（選ぶ／選ばない）
  total = 0
  for i in range(N):
    if bit & (1 << i): # 1を左iビットずつズラす（1, 2, 4, 8, 16, 32, 64, 128...）＝2進数の桁になっている
      total += A[i]
  if total == S:
    print("Yes")
    exit()
print("No")



"""
B問題_部分和問題（動的計画法）
難しい
選ぶ／選ばない
N個の数列の中からいくつか選びその和をKにできるか。

ナップザック問題の典型
二次元配列のdpで行列の足し算をし計算結果を再利用をすることを繰り返す
"""

N,K = map(int, input().split())

dp = [[False] * (K + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  ai = int(input())
  for k in range(K + 1):
    if dp[i - 1][k]:
      dp[i][k] = True
    if k >= ai and dp[i - 1][k - ai]:
      dp[i][k] = True
    
print("Yes" if dp[N][K] else "No")


"""
部分和問題 (余剰計算)（動的計画法）・・・解けた
難しい
"""

N,K = map(int, input().split())

dp = [[False] * (K + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  ai = int(input())
  for k in range(K + 1):
    if dp[i - 1][k]:
      dp[i][k] = True
    if k >= ai and dp[i - 1][(k - ai) % 1000]:
      dp[i][k] = True
    
print("Yes" if dp[N][K] else "No")


"""
最小個数部分和問題・・・解けない
難しい
"""

N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

INF = 10**9
dp = [INF] * (K + 1)
dp[0] = 0

for a in A:
    for k in range(K, a - 1, -1):  # 逆順で更新（重複防止）
        dp[k] = min(dp[k], dp[k - a] + 1)

if dp[K] <= M:
    print("Yes")
else:
    print("No")
