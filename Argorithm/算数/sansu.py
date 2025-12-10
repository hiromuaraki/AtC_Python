import math

"""
問題A_424_Isosceles
二等辺三角形かどうかを判定
二辺が等しいかどうかの場合分け
"""

A,B,C=map(int, input().split())
print("Yes" if A==B or B==C or C==A else "No")


"""
問題A_423_ScrayFee・・・解けない（算数）
難易度

問題を数式に落とす力

1000円あたりC円の手数料が加算

最大でいくら引き出せるか
残高//（1000円＋手数料）*1000（整数除算：小数点以下切り捨て）
"""

X,C=map(int, input().split())
print(X//(1000+C)*1000)

# 別解（シミュレーション）
ans=0
while True:
  now=ans+1000
  if now+(now//1000*C) > X:
    break
  ans=now
print(ans)


"""
エレベーター・・・解けた
難しい

データ構造：辞書型
方針：
i<9未満の間は9-iをキーに設定
それ以外はi%9+1をキーに設定し隣接フロアのデータ構造を実装
｜S-T｜の絶対値で隣接フロアの距離を計算
"""

S,T=input().split()
E={}
for i in range(18):
  floor=(f"B{9-i}" if i<9 else f"{i%9+1}F")
  E[floor]=i
print(abs(E[T]-E[S]))


"""
問題D_Broken Rounding（要復習）・・・解けた
難易度178

方針：
Xの余りが5以上か否かで切り捨て・切り上げを場合分け
"""

X,K=map(int, input().split())

if X < K:
    print(0)
    exit()
n=X
for i in range(K):
    n%=10
    if n<5:
        X=math.floor(X/10)
    else:
        X=math.ceil(X/10)
    n=X
print(X*10**K)


"""
A問題_193_Discount

定価A円の商品がB円で売られている時の売値は定価の何パーセント引きですか？

(1 - 商品価格 / 定価) * 100
"""

A,B = map(int, input().split())
print("{:.5f}".format((1 - B / A)*100))


"""
A問題_NewYear
時間の計算

時→分に変換

次の年＝2日後（24*60*2=2880)
x = （次の年 - M*60）//60
"""

M = int(input())
print((24*60*2 - M*60)//60)

"""
合計時間 (Total Time)
時間の計算
秒を分に変換
分と秒数を求める

分＝秒数の合計 // 60
秒＝秒数の合計 ％ 60
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = (a + b + c + d)//60
y = (a + b + c + d) % 60
print(x, y, sep="\n")


"""
A問題_散歩・・・頭使う

A,Bの行動を交互に繰り返す

X回行った時の回数を求める

A：＋３進む
B：−２戻る

Xが偶数の場合：X//2m
Xが奇数の場合：X//2±3m
"""

X = int(input())
if X % 2 == 0: print(X // 2)
else: print(X // 2 + 3)


"""
A問題_249_jogging・・・・解けない
難易度109

周期性＋規則性＋数理処理

・周期ごとの距離
・あまり時間の切り分け

１サイクル長＝ (歩く時間＋休む時間)
進む距離＝ 速さ * 時間

周期＝X // (歩く時間 + 休む時間)
あまり時間＝ X % (歩く時間＋休む時間)
"""

A,B,C,D,E,F,X = map(int, input().split())


def jogging(a, b, c, x):
  # X秒の中で何サイクル分動けるかを計算
  period = x // (a + c) # 1周期
  r = x % (a + c) # 次のサイクルの余り時間
  return (period * a + min(a, r)) * b # 総距離＋a秒未満ならbメートル進む


t = jogging(A,B,C,X)
a = jogging(D,E,F,X)

if t > a: print("Takahashi") 
elif t < a: print("Aoki")
else: print("Draw")



"""
タイムカード ・・・・解けない

時間の計算

時分秒を全て秒に変換して二つの差を取り
再び時、分、秒に直す

時間の計算
-----------------
時間：X / 3600
分：(X / 60) % 60
秒：X % 60
-----------------

"""

T = [list(map(int, input().split())) for _ in range(3)]
h,m,s = 0, 0 ,0
# 3600h + 60m + s 秒数に変換
for i in range(3):
  h1, m1, s1, h2, m2, s2 = T[i]  
  x1 = h1 * 3600 + 60 * m1 + s1
  x2 = h2 * 3600 + 60 * m2 + s2
  x = x2 - x1
  print(x // 3600, (x // 60) % 60, x % 60)


"""
問題A_Competition・・・解けない

式変形
スーバース抜けはスーパー高橋よりいくら安くればいいか

いくら＝ans
ans / z < y / x
このansを求めるには
z * y = ans * x
ansX = zy

両辺をxで割ると
ans = zy / x

zyがXで割り切れる場合は1円だけ安くする
"""

X,Y,Z = map(int, input().split())
ans = (Z * Y) // X
if (Z * Y) % X == 0: ans -= 1
print(ans)


"""
問題A_Painting・・・解けた

切り上げ処理
(a + b - 1)//b

HWの中で大きい方の値で黒く塗るのが最適
"""

H = int(input())
W = int(input())
N = int(input())
X = max(H, W)
print((N + X - 1) // X)


"""
A問題_040_赤赤赤青赤
難易度92

先頭への移動：x - 1
末尾の移動：n - x
min(x - 1, n - x)
"""

n,x = map(int, input().split())
print(min(x - 1, n - x))


"""
A問題_030_勝率計算・・・解けた
難易度140
"""

A,B,C,D = map(int, input().split())
t = B / A
a = D / C
if t == a: print("DRAW")
elif t < a: print("AOKI")
else: print("TAKAHASHI")