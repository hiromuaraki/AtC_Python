"""
葉の個数
(https://algo-method.com/tasks/10318VS0)

葉＝子頂点を持たない頂点のこと
"""

N = int(input())
P = list(map(int, input().split()))

chs = [[] for _ in range(N)]

for v in range(1, N):
    chs[P[v - 1]].append(v)

print(sum(1 for i in range(1, N) if len(chs[i]) == 0))
        