"""
幅優先探索（BFS）
(https://algo-method.com/descriptions/114)
n個の頂点数、m本の辺数
"""

from collections import deque

n,m = map(int, input().split())
g = [[] for _ in range(n)]

# 隣接リスト作成
for _ in range(m):
    a,b = map(int, input().split())
    # 頂点 A から頂点 B への辺を張る（単純無向グラフ：双方向）
    g[a].append(b)
    g[b].append(a)

# 頂点０を始点とする
que = deque([0]) # あとで訪問するためのtodoリスト
visited = [False] * n # 頂点の訪問を管理するフラグ配列
visited[0] = True # 始点は訪問済み
# 頂点が未探索の間 1手〜N-1手まで探索を繰り返す
while que:
    v = que.popleft()
    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in g[v]:
        if not visited[next_v]:
            visited[next_v] = True
            que.append(next_v) # todoリスト
