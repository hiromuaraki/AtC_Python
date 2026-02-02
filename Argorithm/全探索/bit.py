"""
bit演算／bit全探索の基礎

選ぶ／選ばないの２通り＝2^N通り

bit演算する手順
1. 10進数を2進数に変換
2. 論理演算（＆、｜、＾）を使いフラグ＝１が立っているかを計算
本質的にはフラグが立っているとは＝iがbitに含まれるか？ 部分集合であるかを確認している
3. 2進数の桁（左から→ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512. 1024...）
4. 1 << N = 2^N通り ※Nビット（１）左へズラす

AND(&)・・・aとbの両方が1の時のみ1, それ以外は0
OR(|)・・・aもしくはbの片方が1の時1, それ以外は0
XOR(^)・・・aとbの一方が1の時のみ1, それ以外は0

bit全探索の出力結果
ビット全探索とは部分集合を列挙している！
[]
[0]
[1]
[0, 1]
[2]
[0, 2]
[1, 2]
[0, 1, 2]
[3]
[0, 3]
[1, 3]
[0, 1, 3]
[2, 3]
[0, 2, 3]
[1, 2, 3]
[0, 1, 2, 3]
[4]
[0, 4]
[1, 4]
[0, 1, 4]
[2, 4]
[0, 2, 4]
[1, 2, 4]
[0, 1, 2, 4]
[3, 4]
[0, 3, 4]
[1, 3, 4]
[0, 1, 3, 4]
[2, 3, 4]
[0, 2, 3, 4]
[1, 2, 3, 4]
[0, 1, 2, 3, 4]
"""


#  bit演算の基本（AND OR XOR）
print(45 & 25) # 001001
print(45 | 25) # 111101
print(45 ^ 25) # 110100

# シフト演算子
# a番目のフラグが立っている状態(左シフト)
a = 4
print(1 & (1 << a)) # 2^a
b, c = 3, 4
# a番目, b番目, c番目のフラグが立っている状態
print(1 << a | 1 << b | 1 << c)

N = 5
for bit in range(1 << N):
    s = []
    for i in range(N):
        # iがbitに含まれるか＝bitのi番目のフラグが立っているか？
        if bit & (1 << i):
            # 部分集合を追加
            s.append(i)
    print(f"{bit} : {s}", sep="\n")



"""
部分和問題（NP問題）
N個の要素から集合を全列挙し、
総和がKと等しくなる組合せが存在するかを調べる
"""


N, K = map(int, input().split())
A = list(map(int, input().split()))
# bit全探索（部分和問題）
# N=100だと計算量が間に合わないが計算量を改善する場合は
# 動的計画法（DP）で改善できる
for bit in range(1 << N):
    total = 0
    for i in range(N):
        if bit & (1 << i):
            total += A[i]
    if total == K:
        print("Yes")
        exit()
print("No")


"""
問題C_167_Skill UP・・・解けない（全探索）
難易度595
bit全探索

N個の部分集合を列挙

書籍がN冊の中から選ぶ、選ばないの２通りがN-1個＝2^N通り
書籍を番号、0 1 2と考える

[2,1,0]
選ぶ・選ばないの組合せ＝８通り＝2^3＝２^N
(0,0,0)=０冊
(1,0,0)=書籍２を選ぶ
(0,1,0)=書籍１を選ぶ
(0,0,1)=書籍０を選ぶ
(1,1,0)=書籍２,１を選ぶ
(0,1,1)=書籍１,０を選ぶ
(1,0,1)=書籍２,０を選ぶ
(1,1,1)=書籍２,１,０を選ぶ


1<<N = 2^N
1,2,4,8,16,32,64,128...（2進数の桁）

<i番目のbitの位置を特定>
(bit>>i)=i番目のbitを左端へずらす
&1で
1&1＝1を取得＝bitが立っている

ans=10**6を超えるケースがありansが更新されないケースが発生
ans=10**7に設定

"""

N,M,X=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(N)]

ans=10**7
for bit in range(1, 1<<N): # 2^N通り試す
  d=[0]*M
  cost=0
  for i in range(N):
    # 1が立っているビットを左端にずらし1なら&で1を取得
    # i番目のビットの位置を特定
    if (bit>>i)&1:
      cost+=A[i][0]
      for j in range(1, M+1):
        d[j-1]+=A[i][j]
  # 理解度が全てX以上時のみコストを更新
  if all(n>=X for n in d):
    ans=min(ans, cost)

if ans!=10**7:
  print(ans)
else:
  print(-1)


"""
bit全探索・・・まだ理解できない
集合に対する全探索を行う問題
N人を3つのグループに分けたとき、全グループの幸福度の総和が最大になるようにしたい

要素を含む、含まないの2通り＊N-1個
2^N通り試す＝ALL
1<<N = 2^N

計算量：O(4^N)
[0]*(i+1)はダミーデータ、要素数の数調整

"""
N=int(input())
A=[[0]*(i+1)+list(map(int, input().split())) for i in range(N-1)]
# 集合としてあり得るものの個数
ALL=1<<N

happy=[0]*ALL

# nで表現される集合に要素iが含まれるかを判定
def has_bit(n, i):
  return (n & (1 << i) > 0)

# 幸福度の値を前もって計算
for n in range(ALL):
  for i in range(N):
    for j in range(i+1, N):
      if has_bit(n, i) and has_bit(n, j):
        happy[n]+=A[i][j]

ans=-10**100

for n1 in range(ALL):
  for n2 in range(ALL):
    # n1とn2で重複があれば無視する
    if n1&n2 > 0:
      continue
    # 全体集合の中のn3に含まれていない要素を求める
    n3=ALL-1 - (n1|n2)
    ans=max(ans, happy[n1]+happy[n2]+happy[n3])

print(ans)


"""
C問題_427_
"""

N,M = map(int, input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

# 白／黒の塗り方の割り当てを2^N通り試す
ans = M
for bit in range(1 << N):
  delete_count = 0
  for u, v in G:
    if (1 & (bit >> u)) == (1 & (bit >> v)):
      delete_count += 1
  ans = min(ans, delete_count)

print(ans)




'''
問題009_Brute Force 2（組合せの全探索）・・・解けない（土日やる） 

計算量：O(N*2^N）
カードの枚数 N枚
2^N（指数関数）に回増えていく

2^N-1回ループ
P66に記載
1.2進法を利用して選び方に番号を振る
2.選び方の番号を全探索

'''

N, S = map(int, input().split())
A = list(map(int, input().split()))

# ビット演算を使う
for bit in range(1 << N): # 2^N通り試す（選ぶ／選ばない）
  total = 0
  for i in range(N):
    if bit & (1 << i): # 1を左iビットずつズラす（1, 2, 4, 8, 16, 32, 64, 128...）＝2進数の桁になっている
      total += A[i]
  if total == S:
    print("Yes")
    exit()
print("No")


"""
フラグ状態を整数にする

i番目のフラグが立っているか？
1 << F

ビットシフトにより答えを求める
F = 2
出力：4

2^F

32 16 8 4 2 1・・・2進数の桁の総和

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128 ....
"""

F = int(input())
print(1 << F)


"""
フラグ状態を整数値にする（２）
ビッtシフトにより答えを求める
"""

N = int(input())
F = list(map(int, input().split()))
print(sum(1 << F[i] for i in range(30)))


"""
フラグ状態の復元（１）
X番目のフラグが立っているか

i番目のフラグ（１）が立っているか？
N & (1 << i)
"""

N,X = map(int, input().split())
print("Yes" if N & (1 << X) else "No")


"""
フラグ状態の復元（２）
30個のフラグ状態の管理

Nのフラグが立っている個数と位置を答える
"""

N = int(input())
count = 0
lst = []
for i in range(30):
    if N & (1 << i):
        count += 1
        lst.append(i)
print(count)
print(*lst)


"""
難易度6Q
左シフト：*2
右シフト：/2
"""


x = int(input())
b = f"{x:b}"
digit = "0" * (32 - len(b))
bit = digit + b
# XOR 反転
xor = "".join(str(int(b_i) ^ 1) for b_i in bit)

# 左右シフトは整数として計算して文字列化
MASK_32 = (1 << 32) - 1  # 32ビット全1マスク
left_shift = bin((x << 1) & MASK_32)[2:].zfill(32)
right_shift = bin(x >> 1)[2:].zfill(32)

print(bit)
print(xor)
print(left_shift)
print(right_shift)