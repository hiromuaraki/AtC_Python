"""
自力回答
有向グラフ
データ構造：隣接行列
"""

N,Q=map(int, input().split())
# フォロー状況を管理する隣接行列を作成
G=[[False]*N for _ in range(N)]

for _ in range(Q):
  query=list(map(int, input().split()))
  a=query[1]-1
  if query[0]==1:
    b=query[2]-1
    # 頂点を0-indexedに調整
    G[a][b]=True
  elif query[0]==2:
    for i in range(N):
      if G[i][a]:
        G[a][i]=True
  else:
    to_follow=[]
    for v,is_follow in enumerate(G[a]):
      if is_follow:
        for i, u_ok in enumerate(G[v]):
          if i!=a and u_ok and i not in to_follow:
            to_follow.append(i)

    # フォローフォローを実行
    for x in to_follow:
      G[a][x]=True


# フォロー状況チェック
for i in range(N):
  ans=""
  for j in range(N):
    ans+=("Y" if G[i][j] else "N")
  print(ans)