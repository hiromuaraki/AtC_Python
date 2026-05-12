"""
深さ優先探索
(https://algo-method.com/tasks/13782pgW)
"""

N,M = map(int, input().split())
G = [[] for _ in range(N)] # 隣接リスト作成

for _ in range(M):
    a,b = map(int, input().split())
    G[a].append(b) # 頂点aに頂点bの辺を張る（有向グラフ）

seen = [False] * N # 頂点vの色が塗られているか管理
def rec(v):
    seen[v] = True
    print(v, end=" ")
    G[v].sort()
    for uv in G[v]:
        if seen[uv]:
            continue
        rec(uv)
rec(0)