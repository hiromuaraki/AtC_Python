from itertools import (
  combinations
)
from collections import (
  Counter,
  deque,
  defaultdict
)

from math import sqrt

'''
全104問
[書籍]問題解決のためのアルゴリズム×数学が基礎からしっかりに身につく本のもんdない

計算量の考え方；ざっくりとオーダー記号で表したPCでの計算回数
一般家庭のPCの目安＝10^9回程度（実行時間2秒以内）
'''

'''
問題0_1-100までの総和
単純に N - 1回の計算が発生する
N=100 100-1 =99回

等差数列
隣りあった数の差が同じ
(初項 + N) * 数列の数 / 2

合計101となる50個のペア
101*50=5050


整数：小数点がつかない数：0, -1, 10（分数は除く）
有理数：整数/整数で表すことのできる数・・・0, -1, 1.0, 10、2/3
実数：数直線上で表すことのできる数・・・・π, 0, -1, 1.0, 10、2/3, √3
正の数：0より大きい数
負の数：0未満の数


指数関数：
a^m * a^n = a^m+n
2^5*2^4 = 2^9

a^m/a^n = a^m-n
2^9/2^5 = 2^4

(a^m)^n = a^mn
(2^5)^3 = 2^5*2^5*2^5 = 2^15

a^mb^m = (ab)^m
2^5*3^5 = 6^5
'''
print((1 + 100)*100//2)

'''
3 3
Σ Σ ij
i=1j=1

(1*1)*(1*2)+(1*3)+(2*1)+(2*2)+(2*3)+(3*1)+(3*2)+(3*3)
'''
result = 0
for i in range(1,4):
  for j in range(1, 4):
    result += (i*j)
print(result)



'''
問題001_Print 5+N（文字式）
'''

print(int(input()) + 5) 

'''
問題002_Sum of 3 Integers（足し算）
'''

A,B,C = map(int, input().split())
print(A+B+C)

'''
問題003_Sum of N Integers（足し算）
'''
N = int(input())
print(sum(list(map(int, input().split()))))


'''
問題004_Product of 3 Integers（掛け算）
'''

A,B,C = map(int, input().split())
print(A*B*C)

'''
問題005_Modulo 100（剰余）
'''

N = int(input())
A = list(map(int, input().split()))
print(sum(A) % 100)


'''
問題006_Print 2N+3（１次関数）
時間計算量：O(1)
'''
N = int(input())
print(2+N+3)



# 計算時間の見積もり
'''
問題007_Number of Multiples 1（線形時間）・・・考え方の整理
時間計算量の問題
時間計算量：O(N）

→(N+1)/2
'''

N,X,Y = map(int, input().split())
# 解法1　O(N)回走査
ans = 0
for i in range(1, N+1):
  if i % X == 0 or i % Y == 0: # 倍数の判定
    ans += 1
print(ans)

# 解法２  N以下のX、Yの倍数の個数を計算で求める
# N＝全体　共通している最小公倍数の個数を引く
# 計算量の改善（集合のベン図をイメージ）
# XまたはYで割れるとは＝XとYの最小公倍数（共通で割れる倍数）で求められる
# 最小公倍数＝X＊Y//最大公約数（X,Y）　→ オーバーフロー対策：X//最大公約数(X,Y)*Y
# N（全体）- N//X（Xで割れる倍数の個数） ＋ N//Y（Yで割れる倍数の個数）ー N//最小公倍数

N,X,Y=map(int, input().split())

def gcd1(x, y):
    if y == 0:  
        return x
    return gcd(y, x%y)

lcm1 = X//gcd1(X, Y)*Y
print(N//X + N//Y - N//lcm1)


'''
問題008_Brute Force 1（全探索）・・・解けた

時間計算量：O(N^2)

1 ≦ N ≦ 1000
N^2通り N*N = 1000*1000 = 1000000 = 10^6回
カードの合計がS以下になる書き方を求める（X）
N=3, S=4の場合
4以下になる組合せは
(1,1)(1,2)(1,3)
(2,1)(2,2)
(3,1)
6通り
'''
ans = 0
N,S = map(int, input().split())
for i in range(1, N+1):
  for j in range(1, N+1):
    if i+j <= S:
      ans += 1
print(ans)

'''
問題009_Brute Force 2（組合せの全探索）・・・解けない＊

解法１：bit全探索 2^N通り
解法２：動的計画法 NS通り

計算量：O(N*2^N）
カードの枚数 N枚
2^N（指数関数）に回増えていく

2^N-1回ループ
P66に記載
1.2進法を利用して選び方に番号を振る
2.選び方の番号を全探索

'''

N,S = map(int, input().split())
A = list(map(int, input().split()))
found = False

# bit全探索の解法O(2^N)
for bit in range(1 << N): # 2^N通り試す（選ぶ／選ばない）
  total = 0
  for i in range(N):
    if bit & (1 << i): # 1を左iビットずつズラす（1, 2, 4, 8, 16, 32, 64, 128...）＝2進数の桁になっている
      total += A[i]
  if total == S:
    found = True
    break

print('Yes' if found else 'No')



# 動的計画法の解法 O(NS)
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

'''
問題010＿Brute Force 2（階乗）
階乗
N=5
5! = 1*2*3*4*5

時間計算量：O(N)
'''
N = int(input())
ans = 1
for i in range(1, N+1):
  ans *= i
print(ans)

# 再帰処理の場合
def f(n: int):
  if n == 1:
    return 1
  return n*f(n - 1)

'''
問題011_Print Prime Numbers（素数）・・・解けた
N以下の素数を出力する

2..N+1回繰り返す

1と自分自身以外に約数を持たない＝約数（割り切れる数が2個）
注）N＋1をしないとN-1になる為Nが含まれない
'''


N=int(input())

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2, N+1):
    if is_prime(i):
        print(i, end=" ")

'''
問題012_Primality Test・・・解けた

時間計算量：O(√N)

素数判定
1..N-1通りまで調べない

方針：
2..√Nまでの範囲で割り切れなければ素数と判定
2,3,5,7→4,9,25,49
'''

N=int(input())

for i in range(2, int(N**0.5)+1):
    if N % i == 0:
        print("No")
        exit()
print("Yes")



'''
問題013_Divisor Enumeration（約数列挙）・・・解けた

計算量を工夫したプログラムにしてください
順序は問わない
時間計算量：O(√N)

方針：
1..√N回繰り返す
Nがiで割れたらiを出力
N//iとiが違うならN//iを出力
'''

N=int(input())

for i in range(1, int(N**0.5)+1):
    if N % i != 0:
        continue
    print(i)
    division = N // i
    if division != i:
        print(division) 

'''
問題014_Factorization（素因数分解）・・・解けた
時間計算量：O(√N lon N)
N**0.5→ルートに変換している
√Nを計算している
0.5＝1/2つまり、ルートを意味する

2..√N回繰り返す
Nを2で割れるだけ割る
Nを3で割れるだけ割る
最後にNが1以外の場合、それを素因数に加える
'''

N = int(input())
ans = []
for i in range(2, int(N**0.5)+1):
  while N % i == 0:
    N //= i
    ans.append(i)
if N >= 2:
  ans.append(N)
print(*ans)


'''
問題015_Calculate GCD（最大公約数）
ユークリッドの互除法
＊再帰処理

時間計算量：O(log(A+B))

大きい数から小さい数で割った余りを書き換える操作を繰り返す
0になった時点で割った数が最大公約数

注意）
2回目のループ以降x,yの値が入れ替わる
'''

A,B = map(int, input().split())

def gcd_(x: int, y: int) -> int:
  if y == 0:
    return x
  return gcd_(y, x % y)
print(gcd_(A, B))

'''
問題016_Greatest Common Divisor of N Integers（最大公約数）・・・解けた
ユークリッドの互除法

2つの最大小約数を計算し次の最大公約数を求めることを繰り返す
前の計算結果と以降の数列の最大小約数を求めることをN-2回繰り返す
'''

N = int(input())
A = list(map(int, input().split()))

def calc_gcd(x: int, y: int) -> int:
  if y == 0:
    return x
  return calc_gcd(y, x % y)

x,y = A[0],A[1]
# 1回目の最大公約数を求める
ans = calc_gcd(x, y)

for i in range(N-2):
  # 最大公約数を求める
  ans = calc_gcd(A[i+2],ans)
print(ans)


'''
問題017_Least Common Multiple of N Integers（最小公倍数）・・・解けた
1回目の最大公約数を求める
Ai * Ai+1 / 最大公約数 = 最小公倍数
1回目の結果を元に同じ処理をN-2回繰り返す
'''

N = int(input())
A = list(map(int, input().split()))

# 最大公約数を求める
def gcd(x: int, y: int) -> int:
  if y == 0:
    return x
  return gcd(y, x % y)

# 最小公倍数を求める
# 1つ目の数 * 2つ目の数 / 最大公約数
def lcm(x: int, y: int, gcd: int) -> int:
  return (x * y) // gcd

x,y = A[0],A[1]
if x < y:
  x,y = y,x
ans = lcm(A[0], A[1], gcd(x, y))

for i in range(N-2):
  ans = (A[i+2] * ans) // gcd(A[i+2], ans)
print(ans)


'''
問題018_Convenience Store 1（場合の数）・・・解けた

場合分け
合計が500円になる組み合わせは
100+400 = 500
200+300 = 500 のみ

100,200,300,400をa,b,c,dとしそれぞれのコインの値段の枚数を数える
a*d = b*c
ad+bcが求める答え

コインの枚数をcount関数でカウントしている

500円になる組合せ
100+400=500
200+300=500

100,200,300,400の4種類
a(100),b(200),c(300),d(400)

a*d + b*c = 500

コインの枚数の分布を取る
100*iで枚数に変換

5
100 300 400 400 200

100*1=100
100*2=200
100*3=300
100*4=400

100, 200, 300, 400
1    1    1    2

1*2+1*1=3
'''

N = int(input())
A = list(map(int, input().split()))

a,b,c,d = 0,0,0,0
for i in range(N):
  if A[i] == 100:
    a += 1
  if A[i] == 200:
    b += 1
  if A[i] == 300:
    c += 1
  if A[i] == 400:
    d += 1
print(a*d+b*c)



# 別解
N=int(input())
A=list(map(int, input().split()))

# コインごとの枚数をカウント
coin = Counter(A)
print(coin[100]*coin[400] + coin[200]*coin[300])

# 下のコードはO(N^2)でTLE
# coin = [A.count(100*i) for i in range(1, N)]
# print(coin[0]*coin[3]+coin[1]*coin[2])  

'''
問題019_Choose Cards 1・・・解けた（場合の数）（要復習）

左から順に同じ色のカードを２枚選ぶ場合の数
x, y, z

各色のカードの枚数のs分布を取る

xC2+yC2+zC2通りの場合の数
＝x(x-1)/2+y(y-1)/2+z(z-1)/2
'''

N = int(input())
A = list(map(int, input().split()))
x, y, z = 0,0,0
for i in range(N):
  if A[i] == 1:
    x += 1
  if A[i] == 2:
    y += 1
  if A[i] == 3:
    z += 1

x = x*(x-1)//2
y = y*(y-1)//2
z = z*(z-1)//2
print(x+y+z)

# 別解
N=int(input())
A=list(map(int, input().split()))

# 各色の件数をカウント
c = Counter(A)
x,y,z = c[1]-1, c[2]-1, c[3]-1
print((c[1]*x)//2 + (c[2]*y)//2 + (c[3]*z)//2)


'''
問題020_Choose Cards 2（全探索）・・・（土日やる）
nC5の組み合わせ ５枚選ぶ
＊異なるn個のものの中からr個選ぶ

時間計算量：O(N^4)
4枚のカードの番号が決まれば残りのカードの番号も分かる
4重ループで実装できる。

Ai+1+Ai+2+Ai+3*Ai+4+Ai+5 = x
Ai+5 = x-Ai+1-Ai+2-Ai+3-Ai+4 
1000 - Ai+1 - Ai+2 - Ai+3+Ai+4 = Ai+5

x = 1000 - (i+j+k+l)

だたし
・同じカードを2回使ってはいけない
・同じ組み合わせの重複のカウントを防ぐ    i < j < k < l < m
'''
N = int(input())
A = list(map(int, input().split()))


N=int(input())
A=list(map(int, input().split()))
ans = 0
# 4199ms
for cards in combinations(A, 5):
  if sum(cards) == 1000:
    ans += 1
print(ans)



count = 0
# 305ms（combinationsより圧倒的に速い）
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            for d in range(c+1, N):
                for e in range(d+1, N):
                    if A[a] + A[b] + A[c] + A[d] + A[e] == 1000:
                        count += 1
print(count)




'''
問題021_Combination Easy（nCr）・・・解けた
nCr = N!/(r!*(n-r)!)

例）N=6 r=2
6!/2!*(6-2)!
=6!/2!*4!
=720/48
=15

N!を求める

r!を求める

N-r!を求める

上記の公式で計算
n!/r*(n-r)!

nPr = r!*nCr

nCr・・・順番を区別しない
nPr・・・順番を区別する
'''

N,R = map(int, input().split())

def func_nr(n):
    func = 1
    for i in range(1, n+1):
        func *= i
    return func

n = func_nr(N)
r = func_nr(R)
n_r = func_nr(N-R)
print(n // (r*n_r))

'''
問題022_Choose Cards 3・・・解けない（要復習）

出目の和期待値＝（青の出目の期待値）＋（赤の出目の期待値）
青の出目の期待値＝（B1+B2+Bn）/ N
赤の出目の期待値＝（R1+R2+Rn）/ N

（B1+B2+Bn）/ N ＋（R1+R2+Rn）/ N
'''

'''
問題023_Dice Expectation・・・（期待値）・・・解けた
＊和の期待値は和となる性質

2つの試行を行う

1番目の試行をX、2番目の試行をYとする
Xの期待値をE[X], Yの期待値をE[Y]とするとき、
X＋Yの期待値 = E[X]+E[Y]

2つの出目の和の期待値＝ (X1+X2+X3..Xn / N) + (Y1+Y2+Y3...Yn) / N

:.12f・・・小数点第12位まで出力するフォーマット指定子
'''

N=int(input())
B=list(map(int, input().split()))
R=list(map(int, input().split()))
print("{:.12f}".format((sum(B)+sum(R))/N))

'''
問題024_Answer Exam Randomly・・・（期待値）・・解けた

合計点数の期待値＝(1問目の点数の期待値) + (2問目の点数の期待値)+...(N問目の点数の期待値)

合計点数の期待値＝Q1/P1 + Q2/P2...+Qn/Pn
'''

N = int(input())
ans = 0.0
for i in range(N):
  P,Q = map(int, input().split())
  ans += Q / P
print('{:.12f}'.format(ans))

'''
問題025_Jiro's Vacation（期待値）・・・解けた

サイコロの確率 1/6

1,2の場合：
1回目が1の目が出る確率・・・1/6
2回目が2の目が出る確率・・・1/6
＊1/6 + 1/6 = 2/6 = 1/3

それ以外の場合（3,4,5,6）
＊1-1/3 = 2/3
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0.0
for i in range(N):
  ans += A[i]*(1.0 / 3.0) + B[i]*(2.0 / 3.0)
print('{:.12f}'.format(ans))

'''
問題026_Coin Gacha・・・解けない （保留）
'''

"""
問題027_MergeSort・・・解けない（要復習）
計算量：O(N log N)

空の列Cを用意する
配列列A、Bを比較し最小の要素を配列Cに移す
"""






'''
動的計画法028_Frog 1・・・解けない（動的計画法）

時間計算量：O(V＋E）
V＝ノード数 E = エッジ数

動的計画法とは＝計算の重複を避けるアルゴリズム（無駄をなくす）

動的計画法のイメージ（以下の３つの特徴を持ったアルゴリズム）
・問題をいくつかの小さな問題に分割
・それぞれの問題の計算結果を表に記録
・同じ問題に対して表から計算結果を参照する

大きな問題を小さな問題に分割し最終的な解を求める
→分割統治法

＊計算の重複を避ける（メモ化）

漸化式
𝐹⁡(𝑛)=𝐹⁡(𝑛−1)+𝐹⁡(𝑛−2)𝐹⁡(0)=0,𝐹⁡(1)=1

4
10 30 40 20


フィナボッチ数列：
f(n) = f(n - 1) + f(n - 2)
a1,a2,a3..an
a1+a2 = a3
i,i+1,i+2...i+N
i+i+1 = 2i+1
'''

'''
||：絶対値
[何かしら整数]：切り捨て

足場１から足場へ移動するコスト＝０
足場１かあ足場iへ移動するコスト＝|i - i+1|
足場１から足場２へ移動するコスト＝|i - i+2|

足場i=1..7まである

N = 7
A = 2,9,4,5,1.6.10

開始
[0, None,None,None,None,None,None]

i = 1
dp[0] + |2-9| = 7
[0, 7,None,None,None,None,None]

i = 2..7まで繰り返す
ノード2から来る方法
dp[i - 1] + |9-4| = 12

ノード1から一つ飛ばして来る方法
dp[i - 2] + |2-4| = 2

最小値の比較（min）
最小値は2だから、2をdpに記録
[0, 7, 2,None,None,None,None]

i = 3
ノード3から来る方法
dp[i - 1] + |4-5| = 3

ノード2から一つ飛ばして来る方法
dp[i - 2] + |9-5| = 11

最小値の3を記録
[0, 7, 2, 3,None,None,None]

i = 4
ノード4から来る方法
dp[i - 1] + |5-1| = 7

ノード3から一つ飛ばして来る方法
d@[i - 2] + |4-1| = 5

最小値の3を記録
A = 2,9,4,5,1.6.10
[0, 7, 2, 3, 5,None,None]

i = 5
ノード5から来る方法
dp[i - 1] + |1-6| = 10

ノード4から一つ飛ばして来る方法
d@[i - 2] + |5-6| = 4

最小値の4を記録
[0, 7, 2, 3, 5, 4,None]

i - 6
ノード6から来る方法
dp[i - 1] + |6-10| = 8

ノード5から来る方法
dp[i - 2] + |1-10| = 14

最小値の8を記録
[0, 7, 2, 3, 5, 4, 8]

最小回数＝８
'''

# 他の人の解法
N = int(input())
A = list(map(int, input().split()))
dp = [0]*N
# 動的計画法
for i in range(1, N):
  if i == 1:
    dp[i] = dp[i - 1] + abs(A[i - 1] - A[i])
    continue
  dp[i] = min(dp[i - 1] + abs(A[i - 1] - A[i]),
              dp[i - 2] + abs(A[i - 2] - A[i]))
print(dp[N - 1])


'''
問題029_Climb Stairs・・・解けた（動的計画法）＊

dp[n] = dp[n - 1] + dp[n - 2]
→フィナボッチ数列
'''

N = int(input())
dp = [0]*(N+1)
dp[0], dp[1] = 1, 1
for i in range(2, N+1):
  dp[i] = dp[i-1]+dp[i-2]
print(dp[N])


"""
問題030＿ナップサック問題・・・解けない＊
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
dp = [[0] * (W+1) for _ in range(N + 1)]
K = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1): # 品物を一つずつ見ていく
  wi, vi = K[i - 1]
  for w in range(W + 1): # 容量0-Wまで試す
    # 「入れない」場合 → 上の行の値をそのままコピー
    dp[i][w] = dp[i - 1][w]

    # 入れる場合（重さが収まるなら）
    if w >= wi:
        dp[i][w] = max(dp[i][w], dp[i-1][w-wi] + vi)

print(dp[N][W])


# 別解
# ナップサック問題 (0/1) - 1次元DP最適化版
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)  # dp[w] = 容量wでの最大価値

for wi, vi in items:
    # 重要ポイント: wを大きい方から小さい方に回す
    # → そうしないと同じ品物を複数回使ってしまう
    for w in range(W, wi - 1, -1):
        dp[w] = max(dp[w], dp[w - wi] + vi)

print(dp[W])



'''
問題031_Taro's Vacation・・・動的計画法・・・解けない（要復習）
計算量の工夫の問題

2つの一次元配列を用意
 i日目に勉強した場合の実力アップの最大値のdp1
 i日目に勉強しない場合の実力アップの最大値のdp2

勉強した場合の実力の最大値、勉強しない場合の実力の最大値を比較し記録
'''
# これはダメ
N = int(input())
A = list(map(int, input().split()))
m = 0
for i in range(N-2):
  if m < A[i] + A[i+2]:
    m = A[i] + A[i+2]
print(m)

# 解法
N = int(input())
A = list(map(int, input().split()))
dp1 = [0] * (N + 1) # i日目に勉強する場合実力のアップの最大値
dp2 = [0] * (N + 1) # i日目に勉強しない場合の実力アップの最大値
dp1[0] = 0
dp2[0] = 0
for i in range(1, N + 1):
  dp1[i] = dp2[i - 1] + A[i - 1]
  dp2[i] = max(dp1[i - 1], dp2[i - 1])

print(max(dp1[N], dp2[N]))


'''
問題032_Binary Search（二分探索）・・・解けた
時間計算量：O(log N）
ソート：O(N log N)
あらかじめ昇順または降順のデータに対して使うアルゴリズム
'''

N,X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

left, right = 0, len(A)
is_find = False
while left < right:
  mid = (left + right)//2
  if A[mid] == X:
    is_find = True
    break
  elif A[mid] > X:
    right = mid
  else:
    left = mid + 1

print("Yes" if is_find else "No")


"""
問題033_distance・・・解けない（ベクトル）要復習
難しい

ユークリッド距離（２点間の距離）
√(x2-x1)^2 + (y2-y1)^2

点と点の距離＝ユークリッド距離
｜AB|＝√(ax - bx)^2 + (ay - by)^2

点と直線の距離＝ベクトル（垂線を下ろして計算）
内積＋外積

内積：
ax * bx + ay * by

外積：
|ax * by - ay * bx|

平行四辺形の面積（S）＝底辺＊高さ
外積の性質
・外積の大きさは２つのベクトルが作る平行四辺形の面積と必ず一致する

点と線分の距離＝垂線が線分内にあるか外にあるかで場合分け

線分を B + t*(C-B) という形で表現

1. ベクトルを作る（BA と BC）
2. 内積で 射影係数 t を求める（A が BC に対してどの位置に射影されるか）
3. t が 0〜1 なら射影点が線分上 → 射影点までの距離が答え
4. t が 0 より小さければ最近点は B、1 より大きければ最近点は C → 端点との距離が答え
"""

# 他の人の解法（sigtsuna）
def calc_vector(x1, y1, x2, y2):
    return x2 - x1, y2 - y1

def calc_dist(dot, line):
    ax, ay = dot
    bx, by, cx, cy = line
    # ベクトルを定義
    BAx, BAy = calc_vector(bx, by, ax, ay)
    BCx, BCy = calc_vector(bx, by, cx, cy)
    CAx, CAy = calc_vector(cx, cy, ax, ay)
    CBx, CBy = calc_vector(cx, cy, bx, by)

    if BAx * BCx + BAy * BCy < 0:
        return (BAx * BAx + BAy * BAy)**0.5
    if CAx * CBx + CAy * CBy < 0:
        return (CAx * CAx + CAy * CAy)**0.5
    
    s = abs(BAx * BCy - BAy * BCx)
    l = (BCx*BCx + BCy * BCy)**0.5
    return s/l

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

dist = calc_dist((ax, ay), (bx, by, cx, cy))

print("{:.12f}".format(dist))


"""
問題034_Nearrest Points・・・解けた
ユークリッド距離（２点間の距離）

計算量：O(N^2)

N個の点の距離をN^2通り計算しその中で最小の距離を求める
"""

from math import sqrt

N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]

dist = 1e9
for i in range(N):
  x1, y1 = dot[i]
  for j in range(i, N - 1):
    x2, y2 = dot[j + 1]
    dist = min(dist, sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2))
print(dist)



'''
問038_How Many Guests? ・・・解けた・・階差と累積和（要復習）
時間計算量：O(N+Q）

累積和
計算量：O(N＋Q）

あらかじめイベント日ごとの累積和を計算しておき、
R-Lにてイベント日ごとの差（距離）から来場者数をO(1)で求める
'''

N,Q = map(int, input().split())
A = list(map(int, input().split()))
S=[0]*(N+1)

# イベント日ごとの累積和を求めておく
for i in range(N):
  S[i+1] = S[i]+A[i]

for i in range(Q):
  L, R = map(int, input().split())
  print(S[R]-S[L-1])



"""
問題045_Easy Graph Problem（★2）・・・解けた
グラフアルゴリズム（無向グラフ）
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
問題046_幅優先探索・・・解けた
BFS
"""

from collections import deque

R,C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
S = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dist = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上下左右

sy -= 1; sx -= 1
gy -= 1; gx -= 1

que = deque()
que.append((sy, sx))

while que:
  y,x = que.popleft()
  for dy, dx in dist:
    if visited[y + dy][x + dx] == 0 and S[y + dy][x + dx] == ".":
      visited[y + dy][x + dx] = visited[y][x] + 1
      que.append((y + dy, x + dx))
  if visited[gy][gx] != 0:
    break

print(visited[gy][gx])

"""
問題047_Bipartite Graph（二部グラフの判定）・・・解けない

全ての隣りあった辺が異なるグループ＝二部グラフ
頂点を白（０）黒（１）のグループに分ける


二部グラフ＝隣り合う頂点が異なるグループに分けられるグラフ
頂点を2つのグループに分け、同じグループ同士に辺が存在しない ようにできるグラフ
→隣り合う頂点は異なる色で塗れるか？（２色塗り）

＜頂点同士が異なる色で濡れるか？＞
・隣り合う頂点同士が異なる色
・連結性は関係ない（頂点同士が辺で繋がっていない）

注意）
グラフは「連結性、非連結性」の二部性である為、開始の起点は０固定ではなく
全探索する必要がある。



0: 白
1: 黒
"""


from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
  A,B = map(int, input().split())
  A -= 1; B -= 1
  G[A].append(B)
  G[B].append(A)

color = [-1] * N # 黒色の配列を準備
is_bipartite = True
for start in range(N):
  if color[start] != -1:
   continue
  color[start] = 0
  que = deque([start])
  while que:
    v = que.popleft()
    for nv in G[v]:
      if color[nv] == -1:
        color[nv] = 1 - color[v] # 隣を逆の色に塗る（0⇔1）
        que.append(nv)
      elif color[nv] == color[v]:
        is_bipartite = False
        break
    if not is_bipartite:
      break
  if not is_bipartite:
    break
print("Yes" if is_bipartite else "No")


"""
問題048_small Mulitiple・・・解けない（要解説確認）
今の俺には解けない為解説必須
"""


"""
問題058_Move on Squares 1・・・解けない 
難しい
"""

N,X,Y = map(int, input().split())
d = abs(X) + abs(Y)
if d <= N and d % 2 == N % 2:
  print("Yes")
else:
  print("No")



"""
問題059_Power Of two・・・ほぼ解けた
規則性を見つける

2^Nの一の位を求める
2進数で考えた時に、Nの指数に割り当てていくと
2 - 4 - 8 - 6と周期性がある為、
一の位は2,4,8,6の4パターンのいずれかしかない。


"""

N = int(input())
if N % 4 == 1: print(2)
if N % 4 == 2: print(4)
if N % 4 == 3: print(8)
if N % 4 == 0: print(6)


"""
問題060_StonesGames
頭使う（規則性）

N=4,8の時のみ後手必勝（周期性）
"""

N = int(input())
if N % 4 == 0: print("Second")
else: print("First")

"""
問題063_Move on Squares 2
規則性を見つけるのが難しい
"""

N = int(input())
if N % 2 == 0: print("Yes")
else: print("No")


"""
問題064_All Zero
頭使う（偶奇に着目）
"""

N,K = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
if total % 2 != K % 2 : print("No")
elif total > K: print("No")
else: print("Yes")

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

current_time = 0
ans = 0
for i in range(N):
   if current_time <= A[i][1]:
      current_time = A[i][0]
      ans += 1
print(ans)