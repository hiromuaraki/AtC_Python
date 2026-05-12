"""
辿り着けない頂点
(https://algo-method.com/tasks/1379Xo5o)
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b)

def rec(v: int) -> None:
    for u in G[v]:
        if not visited[u]:
            visited[u] = True
            rec(u)

visited[0] = True
rec(0)

print(visited.count(False))
