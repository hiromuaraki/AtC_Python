"""
兄弟は誰だ？ (2)
(http://algo-method.com/tasks/1051AOEm)
"""

N = int(input())
P = [0] * N # 根（０）を含めN個設定

chs = [[] for _ in range(N)]
# 子頂点リスト作成および親頂点リスト作成
for _ in range(N - 1):
    a,b = map(int, input().split())
    chs[a].append(b)
    P[b] = a

Q = int(input())

for i in range(N):
    chs[i].sort()

for _ in range(Q):
    v = int(input())
    print(*chs[P[v]])
