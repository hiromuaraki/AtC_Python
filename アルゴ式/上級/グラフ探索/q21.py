"""
箱の内部の箱の個数 (1)
(https://algo-method.com/tasks/1108Knxs)
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))
v = int(input())

adj = [[] for _ in range(N)]

for i in range(N - 1):
    adj[A[i]].append(i + 1)

todo = deque([v]) # 始点vを設定
dist = [-1] * N # 到達してない箱を初期化
dist[v] = 0 # 箱vは０手で開けられる

res = 0 # 箱までの移動距離をカウント
# 始点vから到達できる箱があるまで繰り返す
while todo:
    s = todo.popleft()
    for ns in adj[s]:
        if dist[ns] != -1:
            continue
        # 隣接している頂点nsまでの距離を記録
        dist[ns] = dist[s] + 1  
        todo.append(ns)
        res += 1
print(res)