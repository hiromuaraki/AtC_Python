"""
グラフ
計算量：O(N)
"""

# 入力
N, A, B = map(int, input().split())
S = [input() for i in range(N)]

# 出力
print('Yes' if S[A][B] == 'o' else 'No')


"""
フォロー
N：頂点の数（対象物）
M：辺の数（関係性）

有向グラフ（向き有）

グラフ：[[],[],[],[]..]
"""

N,M=map(int ,input().split())
G=[[] for _ in range(N)]

for _ in range(M):
    A,B=map(int, input().split())
    # 有向グラフ
    G[A].append(B)

for follow in G:
    follow.sort()
    print(*follow)
    
    

"""
人気者の友達（無向グラフ）・・・解けた
難しい

向きなし
Aの友達はB
Bの友達はAの双方向の関係
"""

N,M=map(int, input().split())
G=[[] for _ in range(N)]

for _ in range(M):
    A,B=map(int, input().split())
    G[A].append(B)
    G[B].append(A)

mn=0
idx=0
for i in range(N):
    if mn < len(G[i]):
        mn=len(G[i])
        idx=i
print(*sorted(G[idx]))


"""
友達の友達・・・解けた
難しい

無向グラフ
"""
N,M,X=map(int, input().split())
G=[[] for _ in range(N)]

# 無向グラフを作成
for _ in range(M):
    A,B=map(int, input().split())
    G[A].append(B)
    G[B].append(A)

lis=set()
# 頂点vから頂点uへ移動
for v in G[X]:
    for u in G[v]:
        # 頂点uが頂点Xに含まれていない場合は重複を除き追加
        if u!=X and u not in G[X]:
            lis.add(u)

print(len(lis))

"""
グラフ（有向グラフ）・・・解けた
SNS復元
隣接行列
"""

N,Q=map(int, input().split())
graph=[[False]*N for _ in range(N)] 

for _ in range(Q):
    S=list(map(int, input().split()))
    a=S[1]-1
    if S[0]==1:
        b=S[2]-1
        graph[a][b]=True
    elif S[0]==2:
        for v in range(N):
            if graph[v][a]:
                graph[a][v]=True
    else:
        to_follow=[]
        for v in range(N):
            if graph[a][v]:
                for w in range(N):
                    if graph[v][w] and w!=a:
                        to_follow.append(w)
        for w in to_follow:
            graph[a][w]=True

# フォロー状況チェック
for i in range(N):
    ans=""
    for j in range(N):
        ans+=("Y" if  graph[i][j] else "N")
    print(ans)

"""
無向グラフ（隣接リスト）・・・解けた
スプリンクラー
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

"""
問題045_Easy Graph Problem（★2）
"""

N,M = map(int, input().split())
G = [[] * N for _ in range(N)]

for _ in range(M):
  a,b = map(int, input().split())
  a -= 1; b -= 1
  G[a].append(b)
  G[b].append(a)

ans = 0
for i in range(len(G)):
  count = 0
  for v in G[i]:
    if v < i + 1:
      count += 1
  if count == 1:
    ans += count

print(ans)


"""
E問題_Bipartize・・・解けない（要復習）
難易度629
(https://atcoder.jp/contests/adt_easy_20251120_3/tasks/abc427_c)

bit全探索＝2^N通り試す（2進数で考える）

二部グラフとは・・・どの辺についてもその辺が結んでいるふたつの頂点に塗られた色が異なる性質も持つグラフ
色の塗り方を2^N通り試す
"""

N,M = map(int, input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

# 色の塗り方を２^N通り試しそれぞれの辺を見て、
# 結んでいる頂点の色が同じ色だった場合、矛盾するため削除カウントを+1
ans = M
for bit in range(1 << N):
  delete_count = 0
  for v, u in G:
    # nbit右へずらす
    if 1 & (bit >> v) == 1 & (bit >> u):
      delete_count += 1
  ans = min(ans, delete_count)

print(ans)