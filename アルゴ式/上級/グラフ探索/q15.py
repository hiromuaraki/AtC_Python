"""
兄弟は誰だ？ (1)
(https://algo-method.com/tasks/1049gpCF)
"""

N = int(input())
P = list(map(int, input().split()))
Q = int(input())

chs = [[] for _ in range(N)]
for v in range(1, N):
    p = P[v - 1]
    chs[p].append(v)

for _ in range(Q):
    v = int(input())
    v -= 1
    print(*chs[P[v]])
    
