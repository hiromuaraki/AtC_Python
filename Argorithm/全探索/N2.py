"""
jの最高値
"""

N=int(input())
A=list(map(int, input().split()))
m=0
count=0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            m=max(A[i], A[j], A[k])
            if A[j]==m:
                count+=1
print(count)


"""
一の位が等しいペア
"""

L,R=map(int, input().split())
c=set()
for i in range(L,R+1):
    for j in range(L,R+1):
        if i==j:continue
        if i < j and i%10==j%10:
            c.add((i,j))
print(len(c))

"""
友愛数
"""

a,b=map(int, input().split())

def f(n)-> int:
    total=0
    for i in range(1, (n//2)+1):
        if n%i==0:
            total+=i
    return total

if a==b:
    print("No")
    exit()
n1,n2=f(a),f(b)
ans = ("Yes" if n1==b and n2==a else "No")
print(ans)


"""
A問題_165_We Love Golf・・・解けた
A以上B以下の範囲でKの倍数で割れる値があるかを調べる
"""

K=int(input())
A,B=map(int, input().split())
# 全探索の解法
for i in range(A, B+1):
  if i%K==0:
    print("OK")
    exit()
print("NG")


"""
問題B_383_Humidifier 2・・・全探索＋グリッド
難易度272
マンハッタン距離
上下右左（4方向）の移動を想定

(x1,y1), (x2,y2)

|絶対値|
|x1-x2|+|y1-y2|
"""

H,W,D=map(int, input().split())
S=[list(input()) for _ in range(H)]
visited=[[False]*W for _ in range(H)]
# 上下左右の座標
dy=[-1,1,0,0]
dx=[0,0,-1,1]


for i in range(H):
  for j in range(W):
    if not visited[i][j] and S[i][j]==".":
      # 上下左右を確認
      for si,sy in zip(dy, dx):
        y=si+i
        x=sy+j

        if 0<=y<H and 0<=x<W:
          if S[y][x]=="." and abs(i-y)+abs(j-x)<=D:
            visited[y][x]=True

print(visited)


"""
C問題_racecar・・・解けた
難易度70

全探索
"""

N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i == j: continue
    t = S[i] + S[j]
    if t == t[::-1]:
      print("Yes")
      exit()
print("No")


"""
D問題_Playing Cards Validation・・・解けた
難易度60

全探索
"""

N = int(input())
S = [input() for _ in range(N)]
target1 = ("H" ,"D", "C", "S")
target2 = ("A" , "2" , "3" , "4", "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K")
ok = True
for i in range(N):
  for j in range(N):
    if i == j: continue
    if S[i][0] not in target1:
      ok = False
      break
    if S[i][1] not in target2:
      ok = False
      break
    if S[i] == S[j]:
      ok = False
      break
  if not ok:
    print("No")
    exit()

print("Yes")



"""
典型90_055
【全探索・・・定数倍を見積もる】

nC5通り試す
各Aを％Pし先に値を縮小→処理が高速になる
"""
N,P,Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N): # 0
  for j in range(i + 1, N): # 1
    for k in range(j + 1, N): # 2
      for l in range(k + 1, N): # 3
        for m in range(l + 1, N): # 4
            if (A[i]%P * A[j]%P * A[k]%P * A[l]%P * A[m]%P) == Q:
              ans += 1
print(ans)



"""
C問題_Find snuke・・・解けない
難易度352
"""


H,W = map(int, input().split())
S = [input() for _ in range(H)]
# 8方向の座標を用意
# 上下左右左上右下右上左下
table = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
t = "snuke"

for i in range(H):
  for j in range(W):
    # "s"を起点とし8方向の"snuke"の探索を開始
    if S[i][j] != "s": continue
    for di,dj in table:
      ans = []
      for k in range(5): #5文字分チェック
        # kマス進む
        y, x = i + k * di, j + k * dj
        if 0 <= y < H and 0 <= x < W:
          if S[y][x] != t[k]:
            break
          ans.append((y + 1, x + 1))
      if len(ans) == 5:
        for find in ans:
          print(*find)
        exit()


"""
B問題360_Vertical Reading
難易度78

文字列→表に書き込む
"""

S,T = input().split()
N = len(S)
for w in range(N):
  for c in range(w):
    lst = []
    # 縦の行の走査
    for i in range(c, N, w):
      lst.append(S[i])
    if "".join(lst) == T:
      print("Yes")
      exit()
print("No") 


"""
B問題_ Palace・・・解けない（要復習）
難易度211
"""

N = int(input())
T,A = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
dmin = 10**9
for i in range(N):
  d = (T*1000 - H[i]*6) - A*1000
  if d < 0: d = -d
  if dmin > d:
    dmin = d
    ans = i
print(ans + 1)


"""
B問題_No-Divisible Range・・・解けない
難易度5Q
(https://atcoder.jp/contests/abc435/tasks/abc435_b)
難しい
全探索の問題

(l, r)の組を全て試す
1 <= l <= r <= N
l <= i <= r
"""

N = int(input())
A = list(map(int, input().split()))
ans = 0
# 左（先頭）から順に右（端）まで走査し(l, r)の組を試す
for l in range(N): # 0..N(0,1,2,3,N-1)
  S = 0 # rの累積和する変数を用意
  for r in range(l, N): #l..N-1
    S += A[r] # 左端から右端まで累積していく
    ok = True
    for i in range(l, r + 1): # l <= i <= r
      if S % A[i] == 0: # 割った余りが0の時点で(l,r)の組みの条件を満たさない
        ok = False
        break
    # OKの場合は全てのAiがArの約数でない為（割り切れない）条件を満たす
    if ok:
       ans += 1

print(ans)