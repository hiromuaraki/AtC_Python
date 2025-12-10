"""

どんな場面で使うアルゴリズムか？
・同じ計算を何度も繰り返さないための工夫
・全部調べ上げるのは時間がかかりすぎる（全探索）
・部分問題に分けると同じ計算がなん度も出てくる

・部分和問題、最短経路、フィボナッチ数列、ナップサック問題


1. 問題を分割する
例）フィボナッチ数列
F(n) = F(n-1) + F(n-2)

2. 部分問題の再利用
一度求めたF(５）は何度も使うため保存→メモ化

３. 小さい問題から順に計算
0,1から始めて順に計算を積み上げる＝テーブルDP
"""


"""
フィボナッチ数列（漸化式）
難しい
"""

# 再帰なし（２変数のみ）
N = int(input())
a, b = 0, 1

for _ in range(N):
  a, b = b, a + b
print(a)

N,X,Y = map(int, input().split())
fibn = [0] * N
fibn[0], fibn[1] = X, Y

for i in range(2, N):
    fibn[i] = (fibn[i-2] + fibn[i-1])%100
print(fibn[N-1])


"""
フィボナッチ数列のメモ化
"""

N = int(input())

def fib_dp_(n, memo=None):
  if memo is None:
    memo = {}
  
  # すでに計算済みならキャッシュを返す
  if n in memo:
    return memo[n]
  
  if n <= 1:
     return n

  memo[n] = fib_dp_(n - 1, memo) + fib_dp_(n - 2, memo)
  return memo[n]

print(fib_dp_(N))





"""
足場の移動・・・部分和問題

i == 1の時の場合1つ目の移動方法のみ
0 + |A[i] + A[i-1]|

フィナボッチ数列：
f(n) = f(n - 1) + f(n - 2)
a1,a2,a3..an
a1+a2 = a3
i,i+1,i+2...i+N
i+i+1 = 2i+1
'''
"""

# N = int(input())
# H = list(map(int, input().split()))

# dp = [0] * N

# for i in range(1, N):
#     if i == 1:
#         dp[i] = dp[i-1] + abs(H[i-1] - H[i])
#         continue
#     dp[i] = min(dp[i-1] + abs(H[i-1] - H[i]),
#                 dp[i-2] + abs(H[i-2] - H[i]))

# print(dp[N-1])


N = int(input())
H = list(map(int, input().split()))
dp = [0] * N

dp[0] = 0 # 最初にいる足場のコストは0
dp[1] = dp[0] + abs(H[0] - H[1]) # 足場1-2へ移動
for i in range(2, N):
  dp[i] = min(dp[i - 1] + abs(H[i - 1] - H[i]),
              dp[i - 2] + abs(H[i - 2] - H[i - 1]))
              
print(dp[N-1])


"""
マスの移動
"""

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(1, N):
    if i == 1:
        dp[i] = dp[i - 1] + A[i]
        continue
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + 2*A[i])
print(dp[N - 1])

# 別解
# 初期値を設定
dp[1] = A[1]
for i in range(2, N):
    dp[i] = min(dp[i-1] + A[i], dp[i-2] + 2*A[i])
print(dp[N-1])


"""
マスの移動２・・・解けない
"""

N,M = map(int, input().split())
A = list(map(int ,input().split()))
dp = [0] * N

dp[0] = 0 # 初期値を設定
for i in range(1, N):
  for m in range(1, M + 1): # M+1(M以上）
    if i - m >= 0:
      dp[i] = min(dp[i], dp[i - m] + A[i] * m)
print(dp[N - 1])


"""
階段の登り方いくつか求める
N段目を上がる時
i - 1：一段前
i - 2：二段前

dp[N] = dp[N-1] + dp[N-2]
"""

N = int(input())
dp = [0] * (N + 1)

dp[0],dp[1] = 1, 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])

"""
フィボナッチ数列
"""

def fib(n):
   if n <= 1:
      return n
   return fib(n - 1) + fib(n - 2) # 同じ計算を何度もしている

# 動的計画法（同じ計算を何度も繰り返さないよう計算結果をdpテーブルへ記録（メモ化））
# 結果を保存して再利用
def fib_dp(n):
   dp = [0] * (n+1)
   dp[0], dp[1] = 0, 1
   for i in range(2, n+1):
      dp[i] = dp[i - 1] + dp[i - 2]
   return dp[n]

print(fib_dp(5))



N,X,Y = map(int, input().split())
fib_ = [0] * N
fib_[0], fib_[1] = X, Y
for i in range(2, N):
    fib_[i] = fib_[i - 1] + fib_[i - 2]
print(fib_[N - 1] % 100)






"""
問題030＿ナップサック問題・・・解けない
容量W以下で得られる最大の価値をdp[N][W]で求める

N=品物数／W=ナップサックの容量
入力 wi=重さ、vi=価値

(N+1) x (W+1) のDPテーブルを 0 で初期化
上からi番目までの品物を走査
現在見る品物と重さの価値を記録
現在の許容量の重さを調べる

品物iを使う・使わないの２択
使わない → dp[i][w] = dp[i-1][w]

"""

N,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = -10**8
dp = [[INF] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
  wi, vi = A[i - 1]
  for w in range(W + 1):
    # 品物iを使わない場合
    dp[i][w] = max(dp[i][w], dp[i - 1][w])  
    # 品物iを使う
    if w - wi >= 0:
      dp[i][w] = max(dp[i][w], dp[i - 1][w- wi] + vi)
# 一番価値の総和が大きいもの
print(max(dp[N]))

"""
1.1.4 コンビニの問題（ナップサック問題）
S円以内で買い物する時最大何Kcal摂取することができるか
"""

N,S= map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (S + 1) for _ in range(N + 1)]

for i in range(1, N + 1): # 品物を一つずつ見ていく
  price, ka = item[i - 1] # 品物iを記録
  for s in range(S + 1): # 上限0-Sまで
    # 品物を選ばない場合
    # 上の行の値をそのままコピー
    dp[i][s] = dp[i - 1][s]

    # 金額がS円以下なら
    if s >= price:
      dp[i][s] = max(dp[i][s], dp[i - 1][s - price] + ka)
print(dp[N][S])


"""
dp[i][s] = 「最初の i 枚のカードから選んで合計が s にできるか(True/False)」

"""


N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  ai = A[i- 1]
  for s in range(S + 1):
    # カードiを使わない
    if dp[i - 1][s]:
      dp[i][s] = True
    # カードiを使う場合
    # 最初のi-1枚で合計s-aiが作れる
    if s >= ai and dp[i - 1][s - ai]:
      dp[i][s] = True

print("Yes" if dp[N][S] else "No")


"""
すごろく
マスNにたどり着くことは可能か（Yes /No)
マスiにたどり着くことが可能かを記録するDPテーブルを作成
"""

N,M = map(int, input().split())
D = list(map(int, input().split()))
dp = [False] * (N + 1) # マスiに到達できるかを管理
# マス0にははじめから到達している
dp[0] = True

for i in range(1, N + 1): # マスの数
    for j in range(M): # M回サイコロ振る
        if i - D[j] >= 0 and dp[i - D[j]]:
            dp[i] = True
print("Yes" if dp[N] else "No")


"""
部分和問題
N個の数列の中からいくつかを選びその和をKにできるか。
"""

N,K = map(int, input().split())

dp = [[False] * (K + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  ai = int(input())
  for k in range(K + 1):
    if dp[i - 1][k]:
      dp[i][k] = True
    if k >= ai and dp[i - 1][k - ai]:
      dp[i][k] = True
    
print("Yes" if dp[N][K] else "No")


"""
タイルの敷き詰め方・・・解けない
縦幅＝１、横幅＝N の長方形でタイルの積み方は何通りあるか。


dp(N) = dp[i - 1] + dp[i - 2] + dp[i - 3]
N = 3の場合：
1 * N = 3
1 * (N - 1) = 2
1 * (N - 2) = 1

正方形
(1, 1, 1) = 3

長方形
(1, 2) = 3
(2, 1) = 3
(1, 3) = 3

計４通り
""" 

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
  if i - 1 >= 0:
    dp[i] += dp[i - 1]
  if i - 2 >= 0:
    dp[i] += dp[i - 2]
  if i - 3 >= 0:
    dp[i] += dp[i - 3]
print(dp[N])
   

"""
表と数値（貰うDP）・・・解けた

(i - 1, j - 1) 左上
(i - 1, j) 真上
(i - 1, j + 1) 右上 

マスが存在したら
左上＋真上＋右上の総和を埋めていく
"""

A = list(map(int, input().split()))
dp = [[0] * 4 for _ in range(4)]
dp[0] = A
h, w = 4, 4

# 1, 2, 3 行目を順に計算していく
for i in range(1, h):
    for j in range(w):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]
        if i - 1 >= 0:
            dp[i][j] += dp[i -1][j]
        if j + 1 < w:
            dp[i][j] += dp[i - 1][j + 1]
print(dp[h -1][w - 1])


"""
表と数値（２）

"""


N = int(input())
# 配列全体を0で初期化（あらかじめ配列の箱を用意）
dp = [[0] * N for _ in range(N)]
dp[0] = list(map(int, input().split()))

for i in range(1, N):
    for j in range(N):
        # 真上（1から開始必ず真上が存在する）
        dp[i][j] += dp[i - 1][j]
        
        if j - 1 >= 0: # 左上
            dp[i][j] += dp[i - 1][j - 1]
        
        if j + 1 < N: # 右上
            dp[i][j] += dp[i - 1][j + 1]

print(dp[N - 1][N - 1] % 100)


"""
３つの仕事
N日間分のルートを最適化する問題

dp[i][j] = i日目までに得られる報酬の総和

0日目に0, 1, 2の仕事をする場合：
dp[0][0]・・・0の仕事
dp[0][1]・・・1の仕事
dp[0][2]・・・2の仕事

次の日は1, 2しか選べない
max(dp[i - 1][1], dp[i - 1][2])
"""

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

# 0日目の情報を設定
for i in range(3):
    dp[0][i] = A[0][i]

ans = 0
for i in range(1, N):
    dp[i][0] = max(dp[i- 1][1], dp[i - 1][2]) + A[i][0] # i日目に仕事0を行う場合
    dp[i][1] = max(dp[i- 1][0], dp[i - 1][2]) + A[i][1] # i日目に仕事1を行う場合
    dp[i][2] = max(dp[i- 1][0], dp[i - 1][1]) + A[i][2] # i日目に仕事2を行う場合
print(max(dp[N - 1]))

"""
最小個数部分和問題・・・解けない
難しい

N個の数列の中からM個以下を選び和をKにできるか？
"""

N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

INF = 10**9
dp = [INF] * (K + 1)
dp[0] = 0

for a in A:
    for k in range(K, a - 1, -1):  # 逆順で更新（重複防止）
        dp[k] = min(dp[k], dp[k - a] + 1)

if dp[K] <= M:
    print("Yes")
else:
    print("No")


"""
コマの道順・・・解けない
"""

N = int(input())
dp = [[0] * N  for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
print(dp[N - 1][N - 1])


"""
コマの道順（壁あり）・・・解けた
# = 壁
. = 道
"""

N = int(input())
S = [input() for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
           continue
        # 上から来る場合
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        # 左から来る場合
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]

print(dp[N - 1][N - 1])


"""
コマの道順
マスNまでにたどり着くまでのマスの合計の最大

左上のマスから開始
"""

N = int(input())
dp = [[0] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
dp[0] = A[0] # コマの初期値を設定

for i in range(N):
    for j in range(N):
        # 左から
        if j - 1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + A[i][j])
        # 上から
        if i - 1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + A[i][j])
print(max(dp[N - 1]))


"""
コマの道順（逆）

右上のマスから開始
"""

INF = 10**18

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * N for _ in range(N)]
dp[0][N - 1] = A[0][N - 1]

for i in range(N):
    for j in range(N - 1, -1, -1):
        if j + 1 < N:
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + A[i][j])
        if i - 1 >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + A[i][j])
print(dp[N - 1][0])

