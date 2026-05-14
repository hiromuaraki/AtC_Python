"""
箱の内部の箱の個数 (2)
(https://algo-method.com/tasks/1062GC8h)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

chs = [[] for _ in range(N)]

for i in range(N - 1):
    chs[A[i]].append(i + 1)

sub = [1] * N

def dfs(v: int):
    for ch in chs[v]:
        dfs(ch)
        sub[v] += sub[ch]

dfs(0)

for _ in range(Q):
    v = int(input())
    print(sub[v] - 1)


    


