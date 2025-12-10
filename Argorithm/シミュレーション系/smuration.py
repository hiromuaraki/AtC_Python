"""
A問題383_Humidifier 1（シミュレーション）・・・自力AC 2025/9/20
難易度19

★状態管理する為になんの変数が必要かを整理
現在の水の量を保持する変数 water
一つ前の時刻を保持する変数 pre_t

max(0, 現在の水の量-(現在の時刻-前の時刻))
負の値であっても最大0の扱いとする
"""

N=int(input())
water=0
pre=0

for i in range(N):
  time,v=map(int, input().split())
  water=max(0, water-(time-pre))
  water+=v
  pre_t=time
print(water)


"""
問題C_Batters・・解けない
難易度83

前から順に走査すると移動後もチェックするバグになる
その為、後ろから順に0まで見ていき、j+Ai<4ならシミュレーションを行う。
それ以外は右に移動ができないので溢れたものをカウントする
"""
N=int(input())
A=list(map(int, input().split()))
P=[False]*(N+1)
p=0
for i in range(N):
  P[0]=True
  for j in range(N-1, -1, -1):
    if P[j]:
      P[j]=False
      if j+A[i]<4:
        P[j+A[i]]=True
      else:
        p+=1
print(p)


"""
A問題_Shampoo・・・シミュレーション
難易度
"""

V,A,B,C = map(int, input().split())
L = [A, B, C]
K = {0 : "F", 1: "M", 2: "T"}
i = 0
while V >= L[i]:
  V -= L[i]
  i = (i + 1) % len(L)

print(K[i])


"""
A問題_428_解けない
状態遷移の整理、管理が苦手

必要な変数を書き出す
"""

S,A,B,X = map(int, input().split())
ans = 0
# 移動秒数を求める
ans += X // (A + B)*A
ans += min(A, X % (A + B))
print(ans * S)


S,A,B,X = map(int, input().split())

ans = 0
for time in range(X):
  if time % (A + B) < A:
    ans += S
print(ans)


N,A,B,K = map(int, input().split())
# 右から開始
# A-Bの周期性＝１サイクルの変化
# 偶奇に着目
# K//2＝サイクル回数（K回繰り返す）
# A＋（右）,Bー（左）交互に進む
# ２ステップごとにA-B進む
if K % 2 == 0:
  print((A - B) + K//2)
else:
  print((A - B) * (K // 2) + A * (K % 2))


# 左（B）から開始
A,B,K = map(int, input().split())
pos = (A - B) * (K // 2)
if K % 2 == 1:
    pos -= B
print(pos)


"""
final_pos = cycle * full_cycles + pos
"""

A,B,C,D,K = map(int, input().split())

remain = K % 4
pos = 0
if remain == 1:
    pos += A
elif remain == 2:
    pos += A - B
elif remain == 3:
    pos += A - B + C
# remain == 0 の場合は何も足さない

print((A - B + C - D) * (K // 4) + pos)


"""
C問題_Find snuke・・・解けない
難易度352
"""

"""
D問題_Glass and Mag・・・もう少し（ほぼ解けた）
シミュレーション
難易度76
"""

K,G,M = map(int, input().split())
mag = 0
glass = 0
for _ in range(K):
  if glass == G:
    glass = 0
  elif mag == 0:
    mag = M
  else:
    pour = min(mag, G - glass)
    glass += pour
    mag -= pour

print(glass, mag)


"""
B問題_Binary Alchemy・・・シミュレーション
難易度84
"""

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
x = 1
for i in range(1, N + 1):
  if x >= i:
    x = A[x -  1][i - 1]
  else:
    x = A[i - 1][x - 1]
print(x)


"""
A問題_firstPlayer・・・・解けた
難易度40
整数の周期性
"""

N = int(input())
S = [input().split() for _ in range(N)]
age = 10**9+1
si = 0
for i in range(N):
  a = int(S[i][1])
  if a < age:
    age = min(age, a)
    si = i

for i in range(N):
  print(S[(si + i) % N][0])


"""
A問題_Sanitize Hands
難易度19
"""

N,M = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for i in range(N):
  M -= H[i]
  if M >= 0:
    ans = i + 1
print(ans)


"""
問題140_Buffet・・・解けない
難易度89

Ciを得るのはAi,Ai＋1の関係が成立（差が1の時のみ）
"""

N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)
for i in range(N - 1):
  if A[i]+1 == A[i + 1]:
    ans += C[A[i]]
print(ans)


"""
B問題_Bounding・・・ギリ解けた
難易度79

Liを先に加算しX以下の領域以下かを判定
"""

N,X = map(int, input().split())
L = list(map(int, input().split()))

count = 1
d = 0
for i in range(N):
  d += L[i]
  if d <= X:
    count += 1
print(count)

"""
JOI_3 つの箱 (Three Boxes)・・・解けた
"""

N = int(input())
S = input()

x, count = 0,0
for i in range(N):
  if S[i] == "L" and x > 0:
    x -= 1
  elif S[i] == "R" and x < 2:
    x += 1

  if x == 2:
    count += 1
print(count)