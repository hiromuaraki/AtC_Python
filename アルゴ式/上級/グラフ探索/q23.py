"""
兄弟は誰だ？ (3)
(https://algo-method.com/tasks/1052IQ3s)
"""
from collections import deque

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

parent = [-1] * N
parent[0] = 0

todo = deque([0])

while todo:
    v = todo.popleft()
    for ch in G[v]:
        if parent[ch] != -1:
            continue
        parent[ch] = v
        todo.append(ch)

chs = [[] for _ in range(N)]

for v in range(1, N):
    chs[parent[v]].append(v)

Q = int(input())
for _ in range(Q):
    v = int(input())
    print(*chs[parent[v]])