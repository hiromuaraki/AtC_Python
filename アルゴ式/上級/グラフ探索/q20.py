"""
木の 2 頂点間の距離
(https://algo-method.com/tasks/12757OsT)
"""

from collections import deque

N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N - 1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

U,V = map(int, input().split())

dist = [-1] * N # 頂点Uからの距離を記録する配列
todo = deque([U]) # 頂点Uを視点とする
dist[U] = 0

while todo:
    s = todo.popleft()
    for ns in adj[s]:
        if dist[ns] != -1:
            continue
        dist[ns] = dist[s] + 1
        todo.append(ns)
print(dist[V])
