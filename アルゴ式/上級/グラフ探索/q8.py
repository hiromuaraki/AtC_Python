"""
連結成分の個数
(https://algo-method.com/tasks/1383rgYL)
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * N

def rec(v: int):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            rec(u)

count = 0 # ひとかたまりの島の数を数える
for i in range(N):
    if not visited[i]:
        rec(i)
        count += 1
print(count)