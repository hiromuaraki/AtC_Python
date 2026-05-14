"""
木の高さ
(http://algo-method.com/tasks/528)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int, input().split()))

chs = [[] for _ in range(N)]
# 親頂点を子頂点リストへ変換
for v in range(1, N):
    p = P[v - 1]
    chs[p].append(v)

dist = [0] * N # 各子頂点の距離を管理
ans = 0

def rec(v: int):
    for ch in chs[v]:
        dist[ch] = dist[v] + 1
        rec(ch)
    global ans
    ans = max(ans, dist[v])

rec(0)
print(ans)
