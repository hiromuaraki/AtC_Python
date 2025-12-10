from queue import Queue
from collections import deque

"""
BFSの基本（幅優先探索）
距離が小さい始点から順に探索していく

dist = 距離
最小のグラフから順にdist + 1ずつ探索していく
データ構造はキュー（先入れ先出し）
訪れた頂点を管理するvisted[False] * Nを用意

N = 頂点の数 E = 辺の本数 S = 始点
"""

N, E, S = map(int, input().split())
# 隣接リストを作成
G = [[] for _ in range(N)]
visited = [False] * N # 頂点を訪問済みかどうかを管理する配列

for _ in range(E):
  v, u = map(int, input().split())
  G[v].append(u)
  G[u].append(v)

# BFS
# 探索待ちの頂点番号を入れるキューを用意
que = deque()
# 始点を追加し頂点番号を訪問済みに変更
que.append(S)
visited[S] = True

# キューを取り出しながら探索
while que:
  v = que.popleft() # 先頭の要素を取り出し削除
  for j in G[v]:
    if not visited[j]:
      visited[j] = True
      que.append(j)



"""
C問題007_幅優先探索・・・解けない
難易度1024
典型グリッドの走査、４近傍（上下右左）の移動の仕方
"""

R,C= map(int, input().split())
sy, sx = map(int, input().split()) # 開始地点
gy, gx = map(int, input().split()) # ゴール
H = [input() for _ in range(R)] # 二次元座標
# -1:未訪問 0:訪問済み
dist = [[-1] * C for _ in range(R)] # 頂点が訪問済みかどうかを管理

# 0-indexedに変更
sy -= 1; sx -= 1
gy -= 1; gx -= 1

# 探索待ちのマスを入れるキューを準備
que = deque()
que.append([sy, sx])
dist[sy][sx] = 0 # 開始地点を訪問済みに変更

# BFS キューを取り出しながら探索
while que:
  y, x = que.popleft()
  # 上下左右のマスを確認
  for dy, dx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
    # マスが存在しない場合は無視
    if not (0 <= dy < R and 0 <= dx < C):
      continue
    # 壁だった場合も無視
    if H[dy][dx] == "#":
      continue
    # マスが未訪問だった場合は距離を更新しキューに入れる
    if dist[dy][dx] == -1:
      dist[dy][dx] = dist[y][x] + 1
      que.append([dy, dx])

print(dist[gy][gx])




"""
深さ優先探索の問題
MLEでAC出来ない為BFS（幅優先探索で実装）
"""

from collections import deque

H,W = map(int, input().split())
S = [input() for _ in range(H)]
visited = [[-1] * W for _ in range(H)] # 訪問済みかどうかを管理

si, sj = 0, 0
gi, gj = 0, 0
# 始点と終点の座標を設定
for i in range(H):
  for j in range(W):
    if S[i][j] == "s":
      si, sj = i, j
    if S[i][j] == "g":
      gi, gj = i, j
  if si != 0 and gi != 0:
    break

que = deque()
que.append([si, sj])
visited[si][sj] = True

# BFS
while que:
  y,x = que.popleft()
  # 上下左右のマスを確認
  for dy, dx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
      if not (0 <= dy < H and 0 <= dx < W):
        continue
      if S[y][x] == "#":
        continue
      if visited[dy][dx] == -1:
        que.append([dy, dx])
        visited[dy][dx] = 0

print("Yes" if visited[gi][gj] == 0 else "No")



"""
問題C_424_New Skill Acquired ・・・解けない
有向グラフ＋BFS

難易度220？
計算量：O(N)



キューの準備:探索を開始するノードをキューに入れます。﻿
ノードの取り出し:キューからノードを一つ取り出します。﻿
隣接ノードの探索:取り出したノードから直接行ける（隣接する）未探索のノードを見つけます。﻿
キューへの追加:見つかった未探索のノードに訪問済みの印をつけ、キューに追加します。﻿
"""

# 公式解法
N=int(input())
graph=[[] for _ in range(N+1)]

for i in range(1, N+1):
  A,B=map(int, input().split())
  graph[A].append(i)
  graph[B].append(i)

visited=[0]*(N+1)
visited[0]=1

def dfs(v):
  visited[v]=1
  for u in graph[v]:
    if not visited[u]:
      dfs(u)

dfs(0)
print(sum(visited)-1)

# 別解
N=int(input())
G=[[] for _ in range(N)]
visited=[False]*N
que=Queue()

for i in range(N):
  A,B=map(int, input().split())
  if A==0:
    # スキル習得済みに変更
    visited[i]=True
    que.put(i)
  else:
    A-=1; B-=1
    G[A].append(i)
    G[B].append(i)

# BFS
while not que.empty():
  # 頂点を取り出す
  v=que.get()
  for i in G[v]:
    if not visited[i]:
      que.put(i)
      visited[i]=True

print(visited.count(True))


"""
E問題_Humidifier 3（要復習）
難易度750
多始点BFS（アルゴリズム）
"""

from collections import deque

H,W,D=map(int, input().split())
S=[input() for _ in range(H)]

# 上下左右の座標
di=[-1,1,0,0]
dj=[0,0,-1,1]

# 多始点BFS
queue = deque()
visited=[[False]*W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j]=="H":
        queue.append((i, j, 0))
        visited[i][j]=True # スタート地点を訪問済みに更新
        
count=0
while queue:
   h,w,dist=queue.popleft() # i,jの場合だと前の最終の値が反映され数が合わない
   if dist>D:
      continue
   count+=1
   
   # 上下左右に到達できるか
   for i in range(4):
      ni=h + di[i]
      nj=w + dj[i]
      if 0<=ni<H and 0<=nj<W:
         if not visited[ni][nj] and S[ni][nj] != "#":
            visited[ni][nj]=True
            queue.append((ni, nj, dist+1))

print(count)



"""
与えられる入力が二部グラフかを判定
無向グラフ

=== 頂点 0 から探索開始（白=0, 黒=1） ===
現在の頂点: 0（色: 0）
隣接リスト G[0] = [1]
  隣の頂点 1 の状態: color[1] = -1
   → 未塗りなので反対の色 1 に塗る

現在の頂点: 1（色: 1）
隣接リスト G[1] = [0, 2]
  隣の頂点 0 の状態: color[0] = 0
  隣の頂点 2 の状態: color[2] = -1
   → 未塗りなので反対の色 0 に塗る
...
最終的な color 配列: [0, 1, 0, 1]
結果: Yes（二部グラフ）

"""

from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]
color = [-1] * N

# 頂点uの隣が頂点v / 頂点vの隣が頂点u 
for _ in range(M):
  u, v = map(int, input().split())
  u -= 1; v -= 1
  G[u].append(v)
  G[v].append(u)


is_bipartite = True
for start in range(N):
  if color[start] != -1:
    continue
  color[start] = 0
  que = deque([start])
  while que:
    v = que.popleft()
    # 今見ている頂点のvの隣の頂点番号
    for nv in G[v]:
      if color[nv] == -1:
        color[nv] = 1 - color[v]
        que.append(nv)
      elif color[nv] == color[v]:
        is_bipartite = False
print("Yes" if is_bipartite else "No")


"""
問題046_幅優先探索
幅優先探索_グリッドマス
スタート地点からゴール地点まで何手でたどり着けるか
"""

"""
問題046_幅優先探索
BFS
"""

from collections import deque

R,C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
S = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dist = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上下左右

sy -= 1; sx -= 1
gy -= 1; gx -= 1

que = deque()
que.append((sy, sx))

while que:
  y,x = que.popleft()
  for dy, dx in dist:
    if visited[y + dy][x + dx] == 0 and S[y + dy][x + dx] == ".":
      visited[y + dy][x + dx] = visited[y][x] + 1
      que.append((y + dy, x + dx))
  if (y, x) == (gy, gx):
    break

print(visited[gy][gx])



"""
E問題_New Skill Acquired・・・解けない（要復習）
難易度424

BFS（幅優先探索）

頂点を全て辿れるか？
到達可能性を調べ上げる
"""

from collections import deque

N = int(input())
G = [[] for _ in range(N)]
visited = [False]*N
que = deque()

for i in range(N):
  a, b = map(int, input().split())
  if a == 0:
    visited[i] = True
    que.append(i)
  else:
    a -= 1; b -= 1
    G[a].append(i)
    G[b].append(i)

# BFS開始
while que:
  v = que.popleft()
  # 隣接している頂点を探索
  # 到達できる頂点がある間はqueに追加
  for u in G[v]:
    if visited[u]: continue
    visited[u] = True
    que.append(u)

print(sum(visited))


"""
E問題_Count Connected Components
グラフ＋BFS
(https://atcoder.jp/contests/abc284/tasks/abc284_c)
連結成分の個数を求める問題
1-2-3 4 5-6
連結成分＝3

{1,2,3}
{4}
{5.6}

連結成分を数えるには
・全頂点に対して未訪問の位置からBFS/DFSを開始し、
 BFS/DFSの開始回数を数える
"""


from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]
visited_ = [False] * N

for _ in range(M):
  v,u = map(int, input().split())
  v -= 1; u -= 1
  G[v].append(u)
  G[u].append(v)


def bfs(start):
  que = deque([start])
  visited_[start] = True
  while que:
    v = que.popleft()
    for u in G[v]:
      if not visited_[u]:
        visited_[u] = True
        que.append(u)

count = 0
for i in range(N):
  if not visited_[i]:
    bfs(i)
    count += 1
print(count)