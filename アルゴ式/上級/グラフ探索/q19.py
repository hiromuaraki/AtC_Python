"""
帰りがけ順
(https://algo-method.com/tasks/1058My4D)
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))
chs = [[] for _ in range(N)]

for i in range(N - 1):
    chs[A[i]].append(i + 1)

def rec(v: int):
    for ch in chs[v]:
        rec(ch)
    print(v, end=" ")

rec(0)