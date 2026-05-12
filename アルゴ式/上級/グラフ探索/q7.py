"""
連結性判定
(https://algo-method.com/tasks/1380ghBC)
たどり着けない頂点が１つでもあれば、連結性ではない。
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# DFSの解法
def rec(v: int):
    for u in G[v]:
        if not visited[u]:
            visited[u] = True
            rec(u)

visited[0] = True
rec(0)
print("No" if False in visited else "Yes")

# BFSの解法
from collections import deque

todo = deque([0])
seen = [False] * N
seen[0] = True

while todo:
    v = todo.popleft()
    for u in G[v]:
        if not seen[u]:
            seen[u] = True
            todo.append(u)

print("No" if False in seen else "Yes")


