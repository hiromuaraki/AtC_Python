"""
子孫の個数
(https://algo-method.com/tasks/434)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
P = list(map(int, input().split()))
chs = [[] for _ in range(N)]

sub = [1] * N # 頂点 v を根とする部分木の頂点数（自分含む）

for v in range(1, N):
    p = P[v - 1]
    chs[p].append(v)

def rec(v: int):
    for ch in chs[v]:
        rec(ch)
        # 帰りがけに実行される
        sub[v] += sub[ch]

rec(0)
for i in range(N):
    print(sub[i] - 1)
    