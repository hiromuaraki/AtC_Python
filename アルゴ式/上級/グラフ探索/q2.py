"""
スモール・ワールド
(https://algo-method.com/tasks/418)
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

from collections import deque

todo = deque([0])
dist= [-1] * N
dist[0] = 0

ans = 0
while todo:
    v = todo.popleft()
    for nv in G[v]:
        if dist[nv] != -1:
            continue
        dist[nv] = dist[v] + 1
        todo.append(nv)
    ans = max(ans, dist[v])
print(ans)