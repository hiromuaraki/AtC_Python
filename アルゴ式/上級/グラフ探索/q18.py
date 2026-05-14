"""
行きがけ順
(https://algo-method.com/tasks/10530S98)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
chs = [[] for _ in range(N)]

for i in range(N - 1):
    chs[A[i]].append(i + 1)

def rec(v: int):
    print(v, end=" ")
    for ch in chs[v]:
        rec(ch)

rec(0)