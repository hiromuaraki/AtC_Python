"""
無向グラフ（隣接リスト）・・・解けた
"""

N,M,Q=map(int, input().split())
G=[[] for _ in range(N)]

# 無向グラフの隣接リストを作成（双方向）
for _ in range(M):
  u,v=map(int, input().split())
  # 頂点を0-indexedに調整
  u-=1; v-=1
  G[u].append(v)
  G[v].append(u)

C=list(map(int, input().split()))

for _ in range(Q):
  query=list(map(int, input().split()))
  x=query[1]-1
  if query[0]==1:
    print(C[x])
    # 頂点xに隣接する頂点の色をxと同じにする
    for v in G[x]:
      C[v]=C[x]
  else:
    y=query[2]
    print(C[x])
    C[x]=y