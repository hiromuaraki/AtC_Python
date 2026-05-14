"""
頂点の深さ
(https://algo-method.com/tasks/529)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int, input().split()))

chs = [[] for _ in range(N)]
# 各子頂点リストを作成
for v in range(1, N):
    p = P[v - 1]
    chs[p].append(v)

dist = [0] * N
# 頂点vを根とし部分木を探索
def rec(v: int):
    for ch in chs[v]:
        dist[ch] = dist[v] + 1
        rec(ch)
rec(0)
print(*dist, sep="\n")
