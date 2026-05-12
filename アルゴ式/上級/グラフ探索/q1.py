"""
頂点を塗る
(https://algo-method.com/tasks/414)

訪問済み + 何手目か = dist
→何手目で訪問したか？？

visited は yes/no 情報
dist は yes/no + 数値情報
dist[頂点番号] = 最短手数
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)] # 隣接リストを作成[[]]（単純無向グラフ）
dist = [-1] * N # 頂点に訪問済みか管理する配列
for _ in range(M):
    A,B = map(int, input().split())
    G[A].append(B) # 頂点Aに頂点Bの辺を張る
    G[B].append(A) # 頂点Bに頂点Aの辺を張る

from collections import deque

# BFS開始
todo = deque([0])  # 頂点の訪問を管理するtodoリスト
dist[0] = 0 # 0手目で頂点0は移動できる
nodes = [[] for _ in range(N)] # 色を塗った頂点番号を管理する配列
nodes[0].append(0) # 頂点0は訪問済み

# 未訪問の頂点がなくなるまで繰り返す
while todo:
    v = todo.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1 # 頂点nvには距離v＋１で到達できる
        nodes[dist[nv]].append(nv) # 距離nv手目で訪れた頂点番号を記録
        todo.append(nv) # 次に訪問する頂点を追加

for k in range(N):
    nodes[k].sort()
    print(*nodes[k])
