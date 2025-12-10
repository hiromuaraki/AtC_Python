"""
１円玉と５円玉

N円支払う時、最低何枚の効果が必要か。

5円＝a, 1円＝b
a + b = N
b = N - a

5円玉の枚数が確定すろと1円玉が決まる
1円玉の使える枚数＝N - a
N // 5 = N枚のうち5円玉が何枚使えるか分かる

"""

N = int(input())

# ベスト
N = int(input())
print(N//5 + N%5)

# 冗長
coin5 = N // 5 # ５円玉の枚数求める
coin1 = N - (coin5 * 5) 
print(coin5 + coin1)


"""
お菓子（１）

Nが偶数の時Nを２で割る
Nが奇数の時Nを１引く
"""

N = int(input())
count = 0
while N > 0:
    count += 1
    if N % 2 == 0:
        N //= 2
    else:
        N -= 1
print(count)


"""
コイン問題

"""

X = int(input())
A = list(map(int, input().split()))

coins = [50, 10, 5, 1]
res = 0

for i in range(4):
    add = X // coins[i]
    add = min(add, A[i])
    X -= coins[i] * add
    res += add
print(res)


"""
お菓子（２）
"""

N = int(input())
count = 0

while N > 0:
    count += 1
    if N % 3 == 0:
        N //= 3
    else:
        N -= 1
print(count)


"""
問題081_Bill Changing Problem・・・解けた
貪欲法

N円の内、10,000円が使える枚数を求める
N // 10000 = 使える枚数
N % 10000 = 残り残金

以上の処理を5,000円、1000円でも繰り返し枚数を足していく
"""

N = int(input())
ans = 0
money = [10000, 5000, 1000]
for i in range(3):
    ans += N // money[i]
    N %= money[i]
print(ans)


"""
問題082_Interval Scheduling Problem（区間スケジューリング問題）
解けない

最も早い終了時刻を選び続ける
"""

N = int(input())
A = []
for i in range(N):
  l,r = map(int, input().split())
  A.append([r, l])

A.sort() # 終了時刻の早い順に並べ替え
print(A)
current_time = 0
ans = 0
for i in range(N):
   if current_time <= A[i][1]:
      current_time = A[i][0]
      ans += 1
print(ans)


"""
巡回セールスマン問題（近似解放）・・・解けない
難しい

移動距離のコストはユークリッド距離で求める
"""

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

# ユークリッド距離を求める
def dist(i, j):
    return ((XY[j][0] - XY[i][0])**2 + (XY[j][1] - XY[i][1])**2)**0.5

visited = set() # すでに訪問済みの頂点を管理
visited.add(0) # 頂点０は訪問済み

res = 0
prev = 0 # 前回の頂点

for i in range(N - 1):        
    min_dist, nex = min([(dist(prev, j), j) for j in range(N) if j not in visited])
    visited.add(nex)
    res += min_dist
    prev = nex
res += dist(prev, 0)
print(res)

"""
C問題_431_Robot Factory・・・解けない
考察はできた
ソート＋貪欲法

軽い頭パーツに軽い体パーツを割り当ててることが最適解
"""

N,M,K = map(int, input().split())
H = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

i,j,count = 0,0,0
while i < N and j < M:
  if H[i] <= B[j]:
    count += 1 # ロボット１体作る
    i += 1 # 次の頭パーツへ移動
    j += 1 # 次の体パーツへ移動
  else:
    j += 1 # H[i] > B[i]の為次の体パーツへ移動
  
  if count == K:
    print("Yes")
    exit()
print("No")


"""
問題C_370__Word Ladder・・・解けない
難易度288

貪欲法

最小回数＋辞書順最小化した文字列を作り出力

・最小回数：文字の異なる個数（ハミング距離）
S!=Tが異なる箇所が入れ替えが発生する最低回数

・辞書順最小化するには
貪欲に先頭の文字を最小化する
その上で2個目以降も順に最小化していき、
min(文字列、文字列)で辞書順の最小化された文字列を取得する



(https://atcoder.jp/contests/abc370/tasks/abc370_c)
"""

S = input()
T = input()
N = len(S)

x = []

# 貪欲法

while S != T: # SとTが等しくなるまで繰り返す
  ns = "z" * N # あり得ない数を設定
  for i in range(N):
    if S[i] != T[i]:
      # 辞書順の最小の文字列を取得
      ns = min(ns, S[:i] + T[i] + S[i + 1:])
  x.append(ns)
  S = ns # 都度最小の文字列に更新する
print(len(x), *x, sep="\n")