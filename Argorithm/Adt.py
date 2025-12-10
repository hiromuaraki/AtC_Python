# 2025 07/29
from collections import (
  Counter, # 出現回数のカウント（重複を除く）キーが存在しない場合は0が返る
  defaultdict, 
  deque, # 先頭と末尾の要素を高速に削除する
)
from math import sqrt
import heapq # 最小の要素を高速に取り出す
# 再帰処理のオーバーフロー対策
import sys
import math
sys.setrecursionlimit(10**6)

'''
問題A_Batting Average
'''

A,B = map(int, input().split())
print('{:.3f}'.format(round(B / A, 4)))

'''
問題B_1-2-4 Test・・・解けた
難易度45

方針：

10進数を2進数へ変換し2進数の桁を掛けた総和を求める
'''

A,B = map(int, input().split())

n,m = A,B
score = [0] * 3
i = 0
while n > 0:
  score[i] = n % 2
  n //= 2
  i += 1

i = 0
while m > 0:
  if score[i] == 0: score[i] = m % 2
  m //= 2
  i += 1

a,b,c = score[0], score[1], score[2]
print(1*a+2*b+4*c)

# 別解(ビット演算)
a,b = map(int, input().split())
print(a | b)


'''
問題C_Cut 0・・・解けた
'''


X = list(input())
while X[-1] == '0': X.pop()
if X[-1] == '.': X.pop()
print(''.join(X))

'''
問題A_Election 2
難易度20
無駄な場合分けをしないために前提条件を確認
少し難しい
'''

N,T,A = map(int, input().split())
if T < A: T,A = A,T
print('Yes' if T > N - (T+A)+A else 'No')

'''
問題B_Capitalized?・・・解けた
難易度21
'''

import re
S = input()
t = re.findall('[A-Z]', S)
print('Yes' if S[0].isupper() and len(t) == 1 else 'No')


'''
問題D_Ticket Gate Log・・・解けた
難易度63

文字列の復元をしたい
復元（i,o）の交互にする為にiまたはoを挿入する最小回数を求める

復元後の末尾は必ず 'o'になる
復元前の文字列の末尾が 'i'の場合は '0'の件数を足す 
'''

S = input()
cnt, target = 0, 'i'
for t in S:
  if t == target:
    target = ('o' if target == 'i' else 'i')
  else:
    cnt += 1

if  S[-1] == 'i':
  cnt += 1
print(cnt)


'''
問題A_chukodai
'''

S = list(input())
a,b = map(int, input().split())
S[a-1],S[b-1] = S[b-1],S[a-1]
print(''.join(S))

'''
問題B_To Be Saikyo・・・解けない
'''

N = int(input())
P = list(map(int, input().split()))
mx = 0
for i in range(1, N):
  mx = max(mx, P[i])

print(max(0, (mx + 1) - P[0]))


N = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if P[0] <= P[i]:
        ans = max(ans, P[i])
print((ans + 1)-P[0] if ans !=0 else ans)

'''
問題C
'''


'''
問題A_ASCII code
'''

N = int(input())
S = {97+i:chr(ord('a')+i) for i in range(26)}
print(S[N])

# 別解
print(chr(int(input())))


'''
問題B_Same
'''

N = int(input())
A = list(map(int, input().split()))
print('Yes' if all(A[i] == A[i+1] for i in range(N-1)) else 'No')

'''
問題C_Minimize Ordering・・・解けた
'''

print(''.join(sorted(input())))

'''
問題D_A..B..C・・・解けた（全探索）
'''

S = input()
n,ans = len(S),0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if i == j or i == k or j == k: continue
            if i < j < k and j - i == k - j:
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    ans += 1
print(ans)



'''
問題A_Required Length
'''
P,L = input(), int(input())
print('Yes' if L <= len(P) else 'No')


'''
問題B_Last_Two_Digits
'''

print(input()[1:])


'''
問題C_Postal Card・・・解けた
難易度45
'''

N,M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0
for i in range(N):
    is_cnt = False
    for j in range(M):
        if S[i][3:] == T[j] and not is_cnt:
            is_cnt = True
            ans += 1
print(ans)

# 別解
N,M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))
print(sum(1 for i in range(N) if S[i][3:] in T))

'''
問題D_Minimize Abs 1・・・解けない
難易度118
'''


'''
問題A_Glutton Takahashi
'''

N = int(input())
S = [input() for _ in range(N)]
for i in range(N-2):
    if S[i] == S[i+1] == 'sweet':
        print('No')
        exit()
print('Yes')


'''
問題B_Seats
'''

N = int(input())
S = input()
ans = 0
for i in range(N-2):
    if S[i] == '#' and S[i+1] == '.' and S[i+2] == '#':
        ans += 1
print(ans)


'''
問題C_Maritozoo・・・解けた
'''

S = [input() for _  in range(3)]
T = input()
ans = ''
for i in T:
    ans  += S[int(i)-1]
print(ans)


'''
問題D_Fill the Gaps・・・ギリ解けない
難易度67
'''

N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    if A[i] < A[i+1]:
        for j in range(A[i], A[i+1]):
            ans.append(j)
    else:
        for j in range(A[i], A[i+1], -1):
            ans.append(j)
ans.append(A[-1])
print(*ans)


'''
問題A_Triple Four
'''

N = int(input())
A = list(map(int, input().split()))
ok = 'No'
for i in range(N-2):
    if A[i] == A[i+1] == A[i+2]:
        ok = 'Yes'
        break
print(ok)

'''
問題B_Digit Machine
'''

A = list(map(int, input().split()))
k = 0
for _ in range(3):
    k = A[k]
print(k)


'''
問題C_Compression・・・解けた
'''

N = int(input())
A = set(list(map(int, input().split())))
print(len(A))
print(*sorted(A))

'''
問題E_Max Ai+Bj・・・溶けた
難易度75
'''

N = int(input())
A = max(list(map(int, input().split())))
B = max(list(map(int, input().split())))
print(A+B)

'''
問題D_Intersection of Cuboids・・・解けない（要復習）
361-B
'''

'''
問題A_Strictly Increasing?
'''

N = int(input())
A = list(map(int, input().split()))
if all(A[i] < A[i+1] for i in range(N-1)):
    print('Yes')
else:
    print('No')

'''
問題B_22222
'''

S = input()
print(''.join([s for s in S if s == '2']))


'''
問題C_Longest Segment・・・解けた（座標）・・・全探索
難易度43
O(N^2)

ユークリッドの距離

√(x1 - x2)^2 + (y1 - y2)^2 →座標の距離

'''

import math
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for p in P:
    for j in range(N-1):
        a = (p[0] - P[j+1][0])**2
        b = (p[1] - P[j+1][1])**2
        ans = max(ans, math.sqrt(a+b))
print('{:.10f}'.format(ans))


'''
問題D_typo・・・解けない（もう少し）
難易度58
'''

S,T = list(input()),list(input())
ans = 'No'
if S == T:
    ans = 'Yes'
for i in range(len(S)-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S == T:
        ans = 'Yes'
    S[i], S[i+1] = S[i+1], S[i]
print(ans)


'''
問題A_11/22 String
'''

N = int(input())
S = input()
ok = True
t = ''
for i in range(N//2):
    if "1" not in S[i:(N//2)+i]:ok = False
    elif S[N//2] != "/": ok = False
    elif "2" not in S[(N//2)+1:(N//2)+2:]: ok = False
    if not ok:
        break

if ok and len(S) % 2 != 0:  
  print('Yes')
else:
  print('No')

'''
問題B_Insert
'''

N,K,X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(K, X)
print(*A)

'''
問題C_Cat
'''

N = int(input())
S = input()
print(S.replace("na","nya"))


'''
問題D_How Many?・・・解けた
難易度53

S^3+1通り走査
'''

S,T = map(int, input().split())
N = S
ans = 0
for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a+b+c<=S and a*b*c<=T:
                ans += 1
print(ans)


'''
問題A_Content too large
'''

N,M = map(int, input().split())
A = list(map(int, input().split()))
print("Yes" if sum(A) <= M else "No")

'''
問題B_Ege Checker2
'''

a,b = map(int, input().split())
print("Yes" if a*2==b or a*2+1==b else "No")
# こっちが最適解
print("Yes" if b//2==a else "No")

'''
問題C_chess960
'''

S = input()
N = len(S)

# 冗長な解法
b = [i for i in range(N) if S[i] == "B"]
r = [i for i in range(N) if S[i] == "R"]

ok = False
for i in range(len(b)-1):
    if b[i] < b[i+1]:
        if (b[i] + b[i+1]) % 2 != 0:
            if "K" in S[r[i]:r[i+1]]:
                ok = True
    
print("Yes" if ok else "No")


# 自分の中の最適解
for i in range(N):
    if S[i] == "B":
        b.append(i)
    elif S[i] == "R":
        r.append(i)
    elif S[i] == "K":
        k = i

if (b[0]+b[1])%2!=0 and r[0] < k < r[1]:
    print("Yes")
else:
    print("No")

'''
問題D_World Meeting・・・解けない（全探索）
難易度171

24通り試す(0-23時)
9-18時に含まれるか

会議の開催時間は1時間ごとの9パターン
24*9=216通り試す

9-10
10-11
11-12
12-13
13-14
14-15
15-16
16-17
17-18
'''

N = int(input())
cnt = [0 for _ in range(24)]

for _ in range(N):
    W,X = map(int, input().split())
    cnt[X] += W
print(cnt)

ans = 0
for i in range(24):
    total = 0
    for j in range(9):
        total += cnt[(i + j)%24]
    ans = max(ans, total)
print(ans)

"""
問題A_cancel_case
"""

S = input()
for i in range(len(S)):
    if S[i].isupper():
        print(i+1)
        break

"""
問題B_Water_Pressure
"""

print(int(input())/100)

"""
問題C_Weak_Password・・・解けない
難易度64
"""

X = list(map(int, input()))

same, step = True, True
for i in range(len(X)-1):
    if X[i] != X[i+1]:
        same = False
    # 次の数字の判定
    if (X[i]+1)%10 != X[i+1]:
        step = False

if same or step:
    print("Weak")
else:
    print("Strong")

"""
問題D_HeavySnake・・・解けた
"""

N,D = map(int, input().split())
A = [list(map(int, input().split())) for _  in range(N)]

k = 1
ans = 0
while k <= D:
    for t,l in A:
        ans = max(ans, t*(l+k))
    print(ans)
    k += 1

"""
E問題_Σ
難易度178

(1+k)*k//2=kの平均を求める
setにAの数列をつっこみ重複を削除する
"""

N,K = map(int, input().split())
A = set(map(int, input().split()))
k = K*(1+K)//2
for x in A:
    if x <= K: k -= x
print(k)


'''
問題A_Contest Result
'''

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in B:
    total += A[i-1]
print(total)

'''
問題B_Sequence of Strings
'''

N = int(input())
ans = [input() for _ in range(N)]
for s in ans[::-1]: print(s)


'''
問題C_Four hidden・・・解けない（全探索）
難易度74

部分文字列が含まれているかどうか
N-M±1通り試す（5パターン）
|U| = 5
'''

T = input()
U = input()
N,M = (len(T)), len(U)
for i in range(N-M+1):
    ok = True
    for j in range(M):
        if T[i+j] != "?" and T[i+j] != U[j]:
            ok = False
    if ok:
        print("Yes")
        exit()

print("No")


"""
問題A_Rearranging ABC 
"""

S="".join(sorted(input()))
print("Yes" if S == "ABC" else "No")


"""
問題B_ Alternately
"""

N=int(input())
S=input()
if all(S[i]!=S[i+1] for i in range(N-1)):
    print("Yes")
else:
    print("No")


"""
問題C_AtCoder Janken 2・・・解けた
難易度54
"""

N=int(input())
J={}
T=0
for _ in range(N):
    S,C=input().split()
    T+=int(C)
    J[S]=C
ans=sorted(J, key=lambda x:(x, len(x)))
print(ans[T%N])


"""
問題D_GridRotation・・・解けない
難易度189

90度回転操作
0,1,2,3の4通り試す
SをTに一致させる最小の操作回数

回転＋上書き

list(zip(*S[::-1]))は右90度回転のPythonのイディオム

zipの結果はタプル型→リストに変換


4
1110
0010
0010
0010

0001
0001
1110
0000
S=[["1110"], ["0010"], ["0010"], ["0010"]]
T=[["0001"], ["0001"], ["1110"], ["0000"]]

1回目
[(0,0,0,1),
 (0,0,0,1),
 (1,1,1,1),
 (0,0,0,0)]

2回目
 [(0,1,0,0),
 (0,1,0,0),
 (0,1,0,0),
 (0,1,1,1)]


3回目
 [(0,0,0,0),
 (1,1,1,1),
 (1,0,0,0),
 (1,0,0,0)]


4回目
 [(1,1,1,0),
 (0,0,1,0),
 (0,0,1,0),
 (0,0,1,0)]
"""

N=int(input())
S=[list(input()) for _ in range(N)]
T=[list(input()) for _ in range(N)]
ans=10**9

# 90度回転を4通り試す
for c in range(4):
    diff_count=0
    # グリッドS、Tの不一致箇所を数える
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                diff_count += 1
    ans=min(ans, diff_count+c)
    # 右に90度回転
    S=list(map(list, zip(*S[::-1])))
print(ans)



"""
問題E_Triple Attack・・・解けない
難易度368

全ての数字が0になるまで数を引いていくゲーム
周期生を使う
"""

N=int(input())
A=list(map(int, input().split()))
T=0
for a in A:
    num=a//5
    T+=num*3
    a-=num*5
    while a>0:
        T+=1
        if T%3==0: a-=3
        else: a-=1
print(T)


"""
問題A_Buildings
"""

N=int(input())
H=list(map(int, input().split()))
for i in range(1,N):
    if H[0] < H[i]:
        print(i+1)
        exit()
print(-1)


"""
問題B_First ABC
"""

N=int(input())
S=input()
C=set()
ans=0
for i in range(N):
    C.add(S[i])
    if len(C) == 3:
        ans=i
        break
print(ans+1)


"""
問題C_Slimes・・・解けた
難易度41
"""

A,B,K=map(int,input().split())
ans=0
total=A
for i in range(A, B):
    total*=K
    ans+=1
    if B <= total:
        break

print(ans)


"""
問題D_Append・・・解けた
難易度43
"""

Q=int(input())
ans=[]

for _ in range(Q):
    q,n=map(int, input().split())
    if q==1:
        ans.append(n)
    else:
        print(ans[-n])


"""
問題E_Peak・・・解けない
難易度292

尺取法を使う

あらかじめ昇順に並べ替える
配列外参照をしない為にr<Nで制御

Arが小さい時だけ右へ進める
"""


N,M=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
ans=0
r=0

for l in range(N):
    while r < N and A[r] < A[l]+M:
        r += 1
    ans=max(ans, r-l)
print(ans)


"""
問題A_FourDigits
"""

N=int(input())
print("{:04d}".format(N))


"""
問題B_Welcome to AtCorderLand
"""

S,T=input().split()
print("Yes" if S=="AtCoder" and T=="Land" else "No")


"""
問題C_NEXT・・解けた
"""

N=int(input())
A=list(map(int, input().split()))
A.sort(reverse=True)

for i in range(N):
    if A[i]!=A[i+1]:
        print(A[i+1])
        exit()

"""
問題D_cat2・・・解けた（全探索）
"""

N=int(input())
S=[input() for _ in range(N)]
C=set()
for i in range(N):
    for j in range(N):
        if i==j:continue
        C.add(S[i]+S[j])
print(len(C))


"""
問題E_Various・・・解けない
難易度211

計算量：O(N)
尺取法

または二分探索法
計算量：O(N log N)
"""

N=int(input())
A=list(map(int, input().split()))

ans,j=0,0
for a in A:
    while j<N and A[j]*2<=a:
        j+=1
    ans+=j
print(ans)

"""
A問題_369
"""

A,B=map(int, input().split())
if A==B:
    print(1)
elif (B+A)%2==0:
    print(3)
else:
    print(2)

"""
B問題_Lucky Direction
"""

D=input()
ans=""
for s in D:
    if s=="N":
        ans+="S"
    elif s=="E":
        ans+="W"
    elif s=="S":
        ans+="N"
    else:
        ans+="E"
print(ans)


"""
C問題_カップリング選抜・・・解けない
難易度

A+B=SはA,Bの片方が確定すればSが一意になる性質を利用する
Aを求める場合：A=S-BでN回走査し出現回数をカウントしていく
存在しないキーの場合は0になる為エラーにならない。

例：累積和＋辞書
例：ペア和カウント
例：2-SUM 問題（まさにこれ）
例：同じ数はまとめる
例：重複を除く
"""

N,S=map(int, input().split())
A=list(map(int, input().split()))
c=Counter()
ans=0

for i in A:
    ans+=c[S-i]
    c[i]+=1
print(ans)

"""
D問題_NumberBox・・・解けない（グリッド）全探索(要復習)
難易度511

計算量：O(N^3)

8方向（上下左右右上下左上下）通り全探索
予め座標を用意
dx=
dy=
"""

N=int(input())
A=[input() for _ in range(N)]
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
ans=["0"]

def dfs(x,y,c,dir):
  ans = []
  while(c):
    c -= 1
    ans.append(A[x][y])
    x = (x + dx[dir])%N
    y = (y + dy[dir])%N
  return ans

for i in range(N):
    for j in range(N):
        for v in range(8):
            ans=max(ans, dfs(i,j,N,v))
            
print("".join(ans))

"""
問題A_flip
"""

S=input()
ans=""
for s in S:
    if s=="0": ans+="1"
    else:ans+="0"
print(ans)

"""
問題B_TLD
"""

print(input().split(".")[-1])

"""
問題C_Misjudge the Time(要復習)
難易度123

方針
"""

"""
問題D_Traveling Takahashi・・・自力AC
難易度65
マンハッタン距離
(a, b)(c, d)

距離＝math.sqrt((a-c)^2+(b-d)^2)
"""
N=int(input())
O=[0, 0]

def f(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

current=O
cost=0.0
for i in range(N):
    x,y=map(int, input().split())
    cost+=f(current, [x,y])
    current=[x, y]

cost+=f(current, O)
print(cost)


"""
C問題_MissJudgeTime・・・解けない（時間）
難易度123

AB：CD→AC：BD

時刻の分解
十の位：H//10
一の位：H%10
"""

H,M=map(int, input().split())

# 時刻が見間違えやすいかチェック
def miss_judge_time(h, m):
    A,B = h//10,h%10
    C,D = m//10,m%10
    AC=A*10+C
    BD=B*10+D
    return AC<=23 and BD<=59

while not miss_judge_time(H,M):
    M+=1
    if M==60:
        H,M,= H+1,0
    if H==24:
        H=0
print(H, M)


"""
問題A_A Recursive Function
"""

N=int(input())
ans=1
for i in range(1,N+1):
    ans*=i
print(ans)

# 別解（再帰）
def f(n):
    if n==0:
        return 1
    return n*f(n-1)

print(f(N))

"""
問題B_Signed Difficulty
"""

X,Y=map(int, input().split("."))
if 0<=Y<=2:
    print(f"{X}-")
elif 3<=Y<=6:
    print(X)
else:
    print(f"{X}+")

"""
問題C_BaseK
"""

K=int(input())
A,B=input().split()
A,B=int(A, K), int(B, K)
print(A*B)

"""
問題D_ Failing Grade
"""

N,P=map(int, input().split())
A=list(map(int, input().split()))
print(sum(1 for a in A if a<P))

"""
問題E_Pigeonhole Query・・・解けない
難易度209

計算量の工夫：データ構造の工夫
・それぞれのハトがどの巣にいるか・・・・pos
・それぞれの巣に何匹のハトがいるか・・・cnt
・ハトが複数いる巣が何個あるか・・・・・ans
を管理する


"""

N,Q=map(int, input().split())
pos=list(range(N+1))
cnt=[0]+[1]*N
ans=0

for _ in range(Q):
    query=list(map(int, input().split()))
    if query[0]==1:
        p,h=query[1:]

        if cnt[pos[p]]==2:
            ans-=1
        cnt[pos[p]]-=1
        pos[p]=h
        cnt[pos[p]]+=1
        
        if cnt[pos[p]]==2:
            ans+=1
    else:
        print(ans)


"""
A問題_Takahashi san
"""
S,T=input().split()
print(S,"san")

"""
B問題_September
"""
print(sum(1 for i in range(12) if len(input())==i))

"""
C問題_ Prefix and Suffix・・・解けた
難易度54
"""

N,M=map(int, input().split())
S=input()
T=input()
if S==T or (S==T[:N] and S==T[-N:]):
    print(0)
elif S==T[:N] and S!=T[-N:]:
    print(1)
elif S==T[-N:] and S!=T[:N]:
    print(2)
else:
    print(3)

"""
D問題_ P(X or Y)・・・解けた
難易度55
"""

X,Y=map(int, input().split())
count=0
for i in range(1, 7):
    for j in range(1, 7):
        if i+j>=X or abs(i-j)>=Y:
            count+=1

print(count/36)


"""
A問題_11/22string・・・・自力AC
難易度31

11/22stringの条件
・1文字目からN+1/2-1までが”１”
・N+1/2（真ん中）が”／”
・N+1/2+1以降が”２”

方針
Tのi番目が”１”の出現する範囲かをi番目がN＋1/2-1未満かで切り分ける
"""

N=int(input())
T=input()
ans=""
for i in range(N):
    if i<((N+1)//2-1) and T[i]=="1":
        ans+="1"
    else:
        if i==N//2:
            ans+="/"
        else:
            ans+="2"

if T==ans:
    print("Yes")
else:
    print("No")

"""
B問題_New Generation ABC
"""

N=int(input())
ans=0
if N<=125: ans=4
elif N<=211: ans=6
else: ans=8
print(ans)

"""
C問題_ Ranking with Ties・・・解けた
難易度41
"""

N=int(input())
P=list(map(int, input().split()))

for i in range(N):
    rank=1
    for j in range(N):
        if P[i]<P[j]:
            rank+=1
    print(rank)


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
E問題_Humidifier 3（要復習）
難易度750
多始点BFS（アルゴリズム）
"""

from collections import deque

H,W,D=map(int, input().split())
S=[input() for _ in range(H)]

# 上下左右の座標
di=[-1,1,0,0]
dj=[0,0,-1,1]

# 多始点BFS
queue = deque()
visited=[[False]*W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if S[i][j]=="H":
        queue.append((i, j, 0))
        visited[i][j]=True # スタート地点を訪問済みに更新
        
count=0
while queue:
   h,w,dist=queue.popleft() # i,jの場合だと前の最終の値が反映され数が合わない
   if dist>D:
      continue
   count+=1
   
   # 上下左右に到達できるか
   for i in range(4):
      ni=h + di[i]
      nj=w + dj[i]
      if 0<=ni<H and 0<=nj<W:
         if not visited[ni][nj] and S[ni][nj] != "#":
            visited[ni][nj]=True
            queue.append((ni, nj, dist+1))

print(count)


"""
A問題_Lexicographic Order
辞書順
s<tで比較する
"""

S,T=input().split()
print("Yes" if S<T else "No")

"""
B問題_Buy a Pen・・・解けた
"""

pen=list(map(int, input().split()))
C=input()
color={"Red":0, "Green": 1, "Blue": 2}
ans=10**2
# 場合分けなし
for i in range(len(pen)):
  if i==color[C]: continue
  ans=min(ans, pen[i])
print(ans)

# ベストプラクティス
R,G,B = map(int, input().split())
C = input()
ans = 0
if C == 'Red':
  ans = min(G, B) 
elif C == 'Green':
  ans = min(R, B)
else:
  ans = min(R, G) 
print(ans)


"""
C問題_Batters・・・解けない（要復習）
難易度83
シミュレーション
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
問題D_tcaF・・・解けた
難易度29
"""

X=int(input())
func=1
for x in range(1, 100):
  func*=x
  if func==X:
    print(x)
    exit()


"""
E問題_
"""



"""
A問題_Welcome to AtCoder Land 2
"""

X=int(input())
if X<=10: print(10)
elif X<=15: print(15)
else: print(17)


"""
B問題_Divisible
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))
for a in A:
  if a%K==0:
    print(a//K, end=" ")

"""
C問題_Sum of Geometric Series・・・解けた
"""

N,M=map(int, input().split())
func=1
for i in range(1,M+1):
    func+=N**i
    if func>10**9:
        print("inf")
        exit()
    
print(func)


"""
D問題_RightRight Triangle・・・解けない（理解できた）
難易度66

方針：
座標から辺の2乗を出してピタゴラスに当てはめる
（直角をはさむ辺）2+（もう一方の直角をはさむ辺）2=（斜辺）2

3辺の長さを出して、一番長い辺（斜辺候補）を見つけ、ピタゴラスの定理が成り立つか確認するため
→距離を計算することでどの辺が斜辺になるかが分かる

前提：
直角三角形は３辺のうち、斜辺が一番長い
残り2本の長さの2乗の和）=（斜辺の長さの2乗）

２点間の距離＝√(x1-x2)^2+(y1-y2)^2

横の差：x1-x2が「横の辺」
縦の差：y1-y2が「縦の辺」

座標から辺の長さを求める方法
＊２点間の距離＝ユークリッド距離
AB^2=(x1-x2)^2+(y1-y2)^2
BC2=(x2​−x3​)2+(y2​−y3​)^2
CA2=(x3​−x1​)2+(y3​−y1​)^2


直角三角形
AB^2+BC^2=CA^2
BC^2+CA^2=AB^2
CA^2+AB^2=BC^2
"""

A=[list(map(int ,input().split())) for _ in range(3)]
x1,y1=A[0]
x2,y2=A[1]
x3,y3=A[2]

# ２点間のユークリッド距離を求め斜辺の長さを確定させる
# ２点間の距離＝√(x1-x2)^2+(y1-y2)^2
def euclid(a,b,c,d):
    # 差の2乗すれば正の数になる為絶対値は不要
    return (a-b)**2+(c-d)**2

# 座標から2点間のユークリッド距離を求める
A=euclid(x1,x2,y1,y2)
B=euclid(x2,x3,y2,y3)
C=euclid(x3,x1,y3,y1)

ans="No"
# 最終的に三平方の定理（a^2+b^2=c^2)で直角かを判定
if A+B==C: ans="Yes"
elif B+C==A: ans="Yes"
elif C+A==B: ans="Yes"
print(ans)

"""
E問題_Minimum Glutton・・・解けない（もう少し）
難易度189

甘さだけに注目する（塩とは分けて考える）
甘さと塩の食べられる最大の位置を求めminを取り、最小値を出力

事前に降順にソートする
"""

N,X,Y=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

def f(a, x):
    a.sort(reverse=True)
    for i in range(N):
        x-=a[i]
        if x<0:
            return i+1
    return len(a)

print(min(f(A, X), f(B, Y)))


"""
A問題_Middle Letter
"""

S=input()
print(S[len(S)//2])

"""
問題B_Water Pressure
"""

D=int(input())
print(D/100)

"""
問題C_Piano 2・・・解けた
難易度105

計算量：O(N）
"""

N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()

for i in range(N+M-1):
  if C[i] in A and C[i+1] in A:
    print('Yes')
    exit()
print('No')


# 別解　全探索（冗長なプログラム）
N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.sort()
C=sorted(A+B)

for i in range(N-1):
    for j in range(N+M-1):
        if A[i:i+2] == C[j:j+2]:
            print("Yes")
            exit()
print("No")


"""
問題D_Get Closer・・・解けた
難易度79

距離＝ユークリッド距離
原点＝(0, 0)
距離（D）＝ √(x1-x2)^2+(y1-y2)^2
"""

import math
A,B=map(int, input().split())
d=math.sqrt(A**2+B**2)
# 別解
# d=math.sqrt(A**2+B**2)
print(A/d, B/d)


"""
問題A_Triple Four
"""

N = int(input())
A = list(map(int, input().split()))
for i in range(N-2):
  if A[i] == A[i+1] == A[i+2]:
    print("Yes")
    exit()
print("No")

"""
問題B_Cyclic
"""

a,b,c = list(input())
print(b+c+a, c+a+b)

"""
問題C_MissingNo・・・解けた
"""

N = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(N - 1):
  if A[i + 1] - A[i] != 1:
    print(A[i]+1)
    exit()

"""
問題D_First Query Problem・・・解けた
"""

N = int(input())
A = list(map(int, input().split()))

Q = int(input())
for _ in range(Q):
  query = list(map(int, input().split()))
  t, k = query[0 : 2]
  k -= 1
  if t == 1:
    A[k] = query[2]
  else:
    print(A[k])

"""
問題E_Standings・・・解けない
難易度605
浮動小数点の誤差を意識できているか？

double, floatを扱う際は誤差を意識する
小数同士の比較ではなく整数にし比較する

Ai/(Ai + Bi) = Aj/(Aj + Bj)
多公式で計算（たすき掛け）

Ai(Aj + Bj) > Aj(Ai + Bi)

多倍長整数型として扱う
⭐️32、64ビットの桁を超えても扱える整数型にしている（多倍長整数）

10**100し計算する
"""


N = int(input())
K = []
for i in range(N):
  A,B = map(int, input().split())
  # 32、64ビットの桁を超えても扱える整数型にしている（多倍長整数）
  K.append((-A * 10**100 // (A + B), i+1)) 

K.sort()

for _, idx in K:
  print(idx, end=" ")

"""
問題A_Median
"""

A = list(map(int, input().split()))
B = sorted(A)
print("Yes" if B[1] == A[1] else "No")


"""
問題B_ManyA+B Problems
"""

N = int(input())
for _ in range(N):
  a,b = map(int, input().split())
  print(a + b)


"""
問題C_Go Straight and Turn Right・・・解けた
少し難しい頭使う
上下左右向きの回転を0,1,2,3で管理
%4で一周したら0に戻るように設計

(x, y) = (横、縦)
上：(0, -1)
下：(0, 1)
左：(-1, 0)
右：(1, 0)
"""

N = int(input())
T = input()
x,y = 0, 0

current = 0
for s in T:
  if s == "S":
    if current == 0: x += 1
    elif current == 1: y -= 1
    elif current == 2: x -= 1
    else: y += 1
  else:
    current = (current + 1) % 4
print(x, y)


"""
問題D_Pizza・・・解けない
難易度183

Pizzaを回転させるのは現在の位置の管理が発生するためめんどくさい
その為Pizzaは回さず、フォークを入れる位置（角度）を反時計回りで考える
角度を求めるには、角度の累積％３６０

昇順をした後、角度の差を求め最大値を出力する（360度含むためN回回す必要あり）
"""

N = int(input())
A = list(map(int, input().split()))

total = 0
cut = [0]
for a in A:
    total += a
    cut.append(total % 360)

cut.append(360)

cut.sort()
ans = 0
for i in range(N + 1):
    ans = max(ans, cut[i + 1] - cut[i])

print(ans)

"""
問題E_MaxEven・・・解けない
難易度167

２要素の和であり得る組合せ：
・偶数＋偶数＝偶数
・偶数＋奇数
・奇数＋偶数
・奇数＋奇数＝偶数

偶奇２つのペアを二次元配列で管理する
ペアが2件以上存在する場合は最大値を更新していく
"""

N = int(input())
A = list(map(int, input().split()))
d = [[], []]

for a in A:
    d[a % 2].append(a)

ans = -1
for i in range(2):
    d[i].sort(reverse=True)
    if len(d[i]) >= 2:
        ans = max(ans, d[i][0] + d[i][1])

print(ans)



"""
A問題_Seats
難易度20
"""

N = int(input())
S = input()

count = 0
for i in range(N - 2):
  if S[i] == S[i + 2] == "#" and S[i + 1] == ".":
    count += 1
print(count)


"""
問題B_Arithmetic Progression
等差数列
"""

A,B,D = map(int, input().split())
for i in  range(A, B + 1, D):
  print(i, end = " ")


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

全探索しなくても解ける
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
E問題_Path Graph?・・・解けない
難易度466
DFS（深さ優先探索）

全頂点が訪問済みになるまで繰り返す（再帰処理）

パスグラフの性質
・次数が1*2, 残り全ての次数が2 2N-2
・連携性（必ず頂点同士が繋がっている＝両方向に行き来できる）


"""

N, M = map(int, input().split())
g = [[] for _ in range(N)]
visited_ = [False] * N

# 隣接リストを作成
for _ in range(M):
  v,u = map(int, input().split())
  v -= 1; u -= 1
  g[v].append(u)
  g[u].append(v)

# 辺の数はN-1
if M != N - 1:
  print("No")
  exit()

# 連結性をチェック
# 全ての頂点が訪問済みになるまで繰り返す
def dfs(s):
  visited_[s] = True
  for j in g[s]:
    if not visited_[j]:
      dfs(j)

dfs(0)
# 全頂点に到達していなければパスグラフではない（連結性がない為）
if not all(visited_):
  print("No")
  exit()

deg1 = sum(1 for i in range(N) if len(g[i]) == 1)
deg2 = sum(1 for i in range(N) if len(g[i]) == 2)

if deg1 == 2 and deg1 + deg2 == N:
  print("Yes")
else:
  print("No")


"""
A問題_Edge Checker 2・・・解けた
算数。頭使う

二分木の構造
右に行くと*2
左に行くと*2+1

二つの頂点が繋がっているかを判定
偶奇に着目

偶数：2n
奇数：2n + 1

上（子）→下（親）
a * 2 == b または a * 2 + 1 == bと等しい場合、

下（親）→上（子）
b // 2 == a
２つの頂点は繋がっている
"""

a,b = map(int, input().split())
if a * 2 == b or a * 2 + 1 == b:
  print("Yes")
else:
  print("No")

print("Yes" if b // 2 == a else "No")


"""
B問題_When?

算数（時間の計算）
＋文字列操作
除算、剰余の使い方と考え方

フォーマット指定子
"""

K = int(input())
h = 21 + (K // 60)
m = K % 60
print("{0:02d}:{1:02d}".format(h, m))

"""
C問題_Not All・・・解けた
難易度50

集合を使う
1以上M以下が含まれない状態＝AとBに差１つ以上ある状態
set(A) - set(B) の差が０の時は1以上M以下の値がAに含まれている
差がある場合はAに1..Mまでの整数が全て含まれていない
"""
N,M = map(int, input().split())
A = list(map(int, input().split()))
K = list(range(1, M + 1))

count = 0
while True:
  if len(set(A)) - len(set(K)) != 0:
    break
  A.pop()
  count += 1
print(count)


"""
問題D_Fibonacci Reversed・・・解けた
難易度55

漸化式
f(n) = f(n - 1) + f(n - 2)

2桁以上の時に逆順にする
＊2桁以上＝10以上のとき＝１桁は逆順にしても影響しないため制御不要
＊計算結果を文字列に変換→逆春にし整数型に変換した結果を配列へ格納することを繰り返す

"""

# 冗長な解法
# 逆順にする制御は不要。1桁で逆順にしても変化為ないため最初から逆順にしていい
# X,Y = map(int, input().split())
# fib = [0] * 10
# fib[0], fib[1] = X, Y
# total = 0
# for i in range(2, 10):
#   total = fib[i - 1] + fib[i - 2]
#   if total >= 10:
#     total = int(str(total)[::-1])
#   fib[i] = total
# print(fib[9])

# 綺麗な解法
X,Y = map(int, input().split())
fibn = [0]*10
fibn[0],fibn[1] = X,Y

for i in range(2,10):
    n = str(fibn[i-2] + fibn[i-1])
    fibn[i] = int(n[::-1])
print(fibn[9])

"""
問題E_Cross・・・解けない（グリッド）
難易度534

問題文が理解できていない
"""


"""
問題A_Takahashi san 2
"""

S = input()
print("Yes" if S[-3:] == "san" else "No")

"""
問題B_Odd Position Sum
"""

N = int(input())
A = list(map(int, input().split()))
print(sum(A[i] for i in range(N) if i % 2 == 0))

"""
問題C_Explore・・・解けた
難易度152
難しい
"""

N, M, T = map(int, input().split()) # M= ボーナス部屋の数、T＝開始時の持ち時間
A = list(map(int, input().split())) # 持ち時間
X = [list(map(int, input().split())) for _ in range(M)]
visited = [False] * N

for i in range(1, N):
  if T > A[i - 1]:
    T -= A[i - 1]
    visited[i] = True
  else:
    visited[i] = False
    break
  if i <= M:
    T += X[i - 1][1]

print("Yes" if visited[N - 1] else "No")


"""
問題D_Counting Arrays・・・解けた
難易度192
頭使う
"""

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
C= set()

for i in range(N):
  C.add(tuple(L[i]))
print(len(C))


"""
E問題_Circular Playlist・・・解けない（要復習）
周期性を考える
難易度131

割り算できないか？
N曲の長さの総和を求める
"""

N,T = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
T %= s
x = 0
for i in range(N):
  if T < x + A[i]:
    print(i + 1, T - x)
    break
  x += A[i]


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
B問題_Generalized ABC
"""

K = int(input())
str = [chr(ord("A") + i) for i in range(K)]
print("".join(str))


"""
問題C_Precondition・・・文字列探索（解けた）
難易度41
問題文が難しいが問題文通りに実装すれば解ける
"""

S = input()
T = input()

for i in range(2, len(S)):
  if S[i].isupper() and not S[i - 1] in T:
    print("No")
    exit()
print("Yes")


"""
問題D_ Multi Test Cases・・・解けた
入力の意味を理解するまでが勝負
難易度
"""

T = int(input())

for i in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  count = 0
  for a in A:
    if a % 2 != 0:
      count += 1
  print(count)


"""
A問題_First Player・・・解けた
少し頭使う
円環、周期性
"""

N = int(input())
idx, age = 0, 10**18
S = [input().split() for _ in range(N)]
for i in range(N):
  A = int(S[i][1])
  if A < age:
    idx = i
  age = min(age, A)

for i in range(N):
  print(S[(idx + i) % N][0])


"""
B問題_Bitwise Exclusive Or
"""

A,B = map(int, input().split())
print(A ^ B)

"""
C問題_ Takahashi's Secret・・・解けない
シミュレーション
"""

N,X = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
X -= 1
know = [False] * N
know[X] = True
for _ in range(N):
  X = A[X]
  if know[X]: break
  know[X] = True

print(know.count(True))


"""
D問題_Santa Claus 1・・・解けた
グリッドの移動

通過した家は"."に更新するのが楽
この問題は
"""

H,W,X,Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = input()
D = {"U": (-1, 0), "D": (1, 0), "L": (0, -1),  "R": (0, 1)}
ans = 0

X -= 1; Y -= 1
a,b = X, Y
for move in T:
  dy, dx = D[move]
  dy, dx = dy + a, dx + b
  if 0 <= dy < H and 0 <= dx < W:
    if S[dy][dx] == "#":
      continue
    if S[dy][dx] == "@":
      ans += 1
      S[dy][dx] = "."
  a,b = dy, dx

print(a + 1, b + 1, ans)


# 修正版（これがベスト）
# 外周が壁（＃）であることが保証されている為範囲の制御が不要
H,W,X,Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = input()
D = {"U": (-1, 0), "D": (1, 0), "L": (0, -1),  "R": (0, 1)}

X -= 1; Y -= 1
ans = 0
for move in T:
  dy, dx = D[move]
  if S[dy + X][dx + Y] == "#":
    continue
  X, Y = dy + X, dx + Y

  if S[X][Y] == "@":
    S[X][Y] = "."
    ans += 1

print(X + 1, Y + 1, ans)


"""
E問題_Move it・・・解けた
難易度36

優先度付きキューを使い最小値を高速に取り出し削除
"""

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
box = defaultdict(list)

for i in range(N):
  box[A[i]].append(W[i])

ans = 0
for key, data in box.items():
  if len(data) == 1 : continue
  box[key].sort()
  while len(box[key]) != 1:
    ans += heapq.heappop(box[key])
    
print(ans)


"""
A問題_12345・・・解けた
難易度43
"""

A = list(map(int, input().split()))
B = list(range(1, 6))
count = 0

for i in range(4):
  if A[i] != B[i]:
    count += 1
    A[i], A[i + 1] = A[i + 1], A[i]
    if abs(A[i] - A[i + 1]) != 1:
      print("No")
      exit()
print("Yes" if count == 1 else "No")


"""
B問題_Alternately
"""

N = int(input())
S = input()
ok = True
for i in range(N - 1):
  if S[i] == S[i + 1]:
    ok = False
    break
print("Yes" if ok else "No")


"""
C問題_Nice Grid・・・解けない
難易度55

チェビシェフ距離
max(|R - X|,|C - Y|)
中心点が（8, 8）
"""

R,C = map(int, input().split())
dist = max(abs(R  - 8), abs(C -  8)) # 中心点（8, 8）からの距離をチェス場距離で計算
print("white" if dist % 2 == 0 else "black")

"""
問題D_CTZ・・・解けた
"""

N = input()
count, b = 0, bin(N)
for i in range(len(b) - 1, -1, -1):
  if b[i] != "0": break
  count += 1
print(count)


"""
E問題_Dango・・・
"""


"""
A問題_369・・・解けた（場合分けの問題）
等差数列（数式変形）
頭使う
"""

A,B = map(int, input().split())

if A == B: print(1)
elif (A + B) % 2 == 0: print(3)
else: print(2)

"""
問題B_Welcome to AtCoder Land
"""

S,T = input().split()
print("Yes" if S == "AtCoder" and T == "Land" else "No")


"""
問題C_typing・・・解けた
難易度55

現在の位置siで管理
"""

S = input()
T = input()
si = 0
for i in range(len(T)):
  if T[i] == S[si]:
    si += 1
    print(i + 1, end= " ")


"""
問題D_Discord・・・解けない（全探索）
難易度112

隣り合う項の座標をN＊Nの表の二次元配列bool型で管理
"""

N,M = map(int, input().split())
A = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
g = [[False] * N for _ in range(N)]

for i in range(M):
  for j in range(N - 1):
    g[A[i][j]][A[i][j + 1]] = True
    g[A[i][j + 1]][A[i][j]] = True

ans = 0
for x in range(N):
  for y in range(x + 1, N):
    if not g[x][y]:
      ans += 1
print(ans)

"""
問題A_ab
"""

N= int(input())
S = input()
if "ab" in S or "ba" in S: print("Yes")
else: print("No")

# 別解
if S.count("ab") != 0 or S.count("ba") != 0:
   print("Yes")
else:
   print("No")

"""
問題B_aaaadaa
"""

N,c1,c2 = input().split()
S = list(input())
for i in range(int(N)):
  if S[i] != c1:
    S[i] = c2
print("".join(S))


"""
問題C_Who is Missing・・・解けた
難易度29
集合
"""

N,M = map(int, input().split())
A = set(map(int, input().split()))
B = set(list(range(1, N + 1)))
C = B - A
print(len(C))
print(*sorted(C))


# 別解
ans = []
for i in range(1, N + 1):
  if i not in A:
    ans.append(i)
print(len(ans))
print(*ans)


"""
問題D_Spot the Difference・・・解けた
難易度34
"""

N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

for i in range(N):
  for j in range(N):
    if A[i][j] != B[i][j]:
      print(i + 1, j + 1)
      exit()

"""
E問題_Rotate Colored Subsequence・・・解けない
難易度342

あらかじめ色ごとにグループ分けする為の配列の配列を作る
"""

N,M= map(int, input().split())
S = input()
C = list(map(lambda x: int(x) - 1, input().split()))
ps = [[] for _ in range(M)]

# 色ごとにグループ分け
for i in range(N):
  ps[C[i]].append(S[i])

ind = [-1] * M
ans = []
for i in C:
  # -1%要素数＝-1で末尾を追加していく
  # 末尾の追加が終わったらind=[0, 0, 0]に更新しており、順に先頭から追加していく
  ans.append(ps[i][ind[i]%len(ps[i])])
  ind[i] += 1
print("".join(ans))

"""
A問題_Signed Difficulty
"""

X, Y  = map(int, input().split("."))
if Y <= 2: print(f"{X}-")
elif Y <= 6: print(f"{X}")
elif Y <= 9: print(f"{X}+")


"""
問題B_Anyway Takahashi
"""

a,b,c,d = map(int, input().split())
print((a + b) * (c - d))
print("Takahashi")

"""
問題C_AtCoder Quiz・・・解けた
難易度22
"""

S = set(input() for _ in range(3))
K = {"ABC","ARC","AGC","AHC"}
print(*K - S)

"""
問題D_Heavy Snake
難易度30
少し頭使う
"""

N,D = map(int, input().split())
T = [input().split() for _ in range(N)]

ans = 0
k = 0
for _ in range(D):
  k += 1
  for t, l in T:
    ans = max(ans, int(t) * (int(l) + k))
  print(ans)

"""
E問題_RANDOM・・・解けない
難易度272

行列の入れ替え＝転置
S[i][j] → S[j][i]
"""

H,W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

# zipの基本挙動は同じ位置のインデックス同士をまとめる関数
# ＊（アンパック演算子）でリストを展開["#", "#", "#"]しタプルにセット
# 同じ位置同士でまとめられ[(S[0][0], S[1][0], S[2][0])...]
# 結果的に転置（行列の入れ替え）(i, j) が(j, i)になっている。
ss = [s for s in zip(*S)]
tt = [t for t in zip(*T)]

ss.sort(); tt.sort()
print("Yes" if ss == tt else "No")


"""
問題A_Five Integers
"""

st = set(map(int, input().split()))
print(len(st))

"""
問題B_Rightmost
"""

S = input()
ans = -1
for i in range(len(S)):
  if S[i] == "a":
    ans = i + 1
print(ans)


"""
C問題_Avoid Rook Attack・・・解けた
グリッド
難易度50
"""

# 良いコード（無駄がなく簡潔）
S = [input() for _ in range(8)]

tate = set()
yoko = set()

for i in range(8):
  for j in range(8):
    if S[i][j] == "#":
      tate.add(i) # 行
      yoko.add(j) # 列

# 行列の出現しない個数が答え
diff_row = 8 - len(tate)
diff_col = 8 - len(yoko)
print(diff_row * diff_col)


S = [input() for _ in range(8)]
row = []
# ダメなコード
for i in range(8):
  for j in range(8):
    if S[i][j] == "#":
      row.append((i, j))

st_row = {0, 1 ,2 ,3, 4, 5, 6, 7}
st_col = {0, 1 ,2 ,3, 4, 5, 6, 7}


if len(row) != 0:
  row_data, col_data = list(zip(*row))
  diff_row = st_row - set(row_data)
  diff_col = st_col - set(col_data)
  print(len(diff_row) * len(diff_col))
else:
  print(64)

"""
問題D_Get Min・・・解けた
難易度31

優先度付きキューを使い最小値を取り出す（データ構造）
"""

import heapq

Q = int(input())
heap = []
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    x = query[1]
    heapq.heappush(heap, x)
  else:
    print(heapq.heappop(heap))


"""
E問題_Perfect Bus・・・解けない（要復習）
難易度171

シミュレーション（くそ苦手）
"""

N = int(input())
A = list(map(int, input().split()))

y, l = 0, 0 # yは高さ lは求めたい最下点
for a in A:
  y += a
  l = min(l, y)
print(y + (-l))


"""
問題A_Not Acceptable・・・時刻の問題・・・解けない
難易度11
"""

A,B,C,D = map(int, input().split())
if (C, D) < (A, B): print("Yes")
else: print("No")

# 分に直すver
if (60*A+B) > (60*C+D): print("Yes")
else: print("No")


"""
問題B_Seismic magnitude scales
"""

A,B = map(int, input().split())
print(32**(A - B))


"""
問題C_Unauthorized・・・解けた
難易度22
"""

N = int(input())
is_login = False
count = 0
for _ in range(N):
  s = input()
  if s == "login":
    is_login = True
  elif s == "logout":
    is_login = False
  elif not is_login and s == "private":
    count += 1
print(count)


"""
問題D_Qualification Contest・・・解けた
辞書順の並べ替え
難易度44
"""

N,K = map(int, input().split())
S = [input() for _ in range(N)]
S = S[:K]
S.sort()
print(*S, sep="\n")


"""
問題E_Count ABC Again・・・解けない
難易度341
"""

N,Q = map(int, input().split())
S = input()

def add(x, count, cnt=1):
  for j in range(x - 2,x + 1):
    if j < 0 or N -1 < j: continue
    if "".join(SS[j:j+3]) == "ABC":
      count += cnt
  return count

# 変更前のABCの件数をカウントしておく
cnt = S.count("ABC")
SS = list(S)
for _ in range(Q):
  x,c = list(input().split())
  x = int(x) - 1
  cnt = add(x, cnt, -1)
  SS[x] = c
  cnt = add(x, cnt)
  print(cnt)


"""
問題A_Swap Odd and Even
2文字ずつに区切りSwap
"""

S = list(input())
for i in range(len(S) // 2):
  S[2*i], S[2*i+1] = S[2*i+1], S[2*i]
print("".join(S))


"""
問題B_GoodMorning・・・解けた
難易度25
"""

A,B,C,D = map(int, input().split())
if 60*A+B < 60*C+D+1: print("Takahashi")
else: print("Aoki")

"""
C問題_Cut.0・・・解けた
難易度43
"""

X = list(input())
while X[-1] == "0":
  X.pop()

if X[-1] == ".":
  X.pop()
print("".join(X))


"""
A問題_T-shirt・・・確率
少し難しい
"""

A,B,C,X = map(int, input().split())
if X <= A:
  print("{:.12f}".format(1))
elif A < X <= B:
  print("{:.12f}".format(C / (B - A)))
else:
  print("{:.12f}".format(0))


"""
B問題_ Hamming Distance
"""

N = int(input())
S = input()
T = input()
count = 0
for i in range(len(S)):
  if S[i] != T[i]:
    count += 1
print(count)


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
E問題_New Skill Acquired・・・解けない（要復習）
難易度424

BFS（幅優先探索）

頂点を全て辿れるか？
到達可能性を調べ上げる
"""

from collections import deque

N = int(input())
G = [[] for _ in range(N)]
visited = [False]*N
que = deque()

for i in range(N):
  a, b = map(int, input().split())
  if a == 0:
    visited[i] = True
    que.append(i)
  else:
    a -= 1; b -= 1
    G[a].append(i)
    G[b].append(i)

# BFS開始
while que:
  v = que.popleft()
  # 隣接している頂点を探索
  # 到達できる頂点がある間はqueに追加
  for u in G[v]:
    if visited[u]: continue
    visited[u] = True
    que.append(u)

print(sum(visited))


"""
A問題_Penalty Kick
"""

N = int(input())
ans = ""
for i in range(1, N + 1):
  if i % 3 == 0: ans += "x"
  else: ans += "o"

print(ans)


"""
B問題_Rearranging ABC
"""

S = input()
S = sorted(S)
print("Yes" if "".join(S) == "ABC" else "No")

"""
C問題_racecar・・・解けた
難易度70

ありうる組わせを全て調べ上げる
回文判定
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
D問題_Dentist Aoki・・・解けた
難易度45
XORで歯を抜く、生やすを表現
1 → 0
0 → 1
"""

N,Q = map(int, input().split())
cnt = [1] * N
T = list(map(int , input().split()))
for i in range(Q):
  cnt[T[i] - 1] ^= 1
print(N - cnt.count(0))


"""
E問題_E - 1 2 1 3 1 2 1・・・解けない
メモ化再帰
難易度149

漸化式：
n == 1: (1)
n ≧ 2: S(n - 1) + [n] + S(n - 1)

辞書型のメモを用意し計算結果を記録
再帰を呼び出さずO(1)で計算結果を呼び出し

漸化式関連は動的計画法、メモ化再帰を実装できないか考察する

"""

N = int(input())

def Sn(n, memo=None):
  if memo is None:
    memo = {}
  
  if n in memo:
    return memo[n]
  
  if n <= 1:
    return [1]
  ret = Sn(n - 1, memo) + [n] + Sn(n  - 1, memo)
  memo[n] = ret
  return ret

print(*Sn(N))


# 他の人の解法
s = [1]                      # S1
for x in range(2, N + 1):    # S2, S3, ... SN を順に作る
    s = s + [x] + s

print(*s)

"""
A問題_Order Something Else・・・解けた
難易度23
"""

N,P,Q = map(int, input().split())
D = list(map(int, input().split()))
ans = P
for d in D:
  ans = min(ans, d + Q)
print(ans) 


"""
B問題_Raise Both Hands
難易度11
"""

L,R = map(int, input().split())
if L > R: print("Yes")
elif L == R: print("Invalid")
else: print("No")

"""
C問題_Second Best・・・解けた
難易度22
"""

N = int(input())
A = list(map(int, input().split()))
B = sorted(A[:], reverse=True)[1]
print(A.index(B) + 1)


"""
D問題_tcaF・・・解けた
難易度25
"""

X = int(input())
ans = 1
for i in range(1, X + 1):
  ans *= i
  if X == ans:
    print(i)
    exit()

"""
E問題_Convex Quadrilateral・・・解けない
難易度516

ベクトル外積の問題
"""

"""
A問題_Strictly Increasing?
"""

N = int(input())
A = list(map(int, input().split()))
if all(A[i] < A[i + 1] for i in range(N - 1)):
  print("Yes")
else:
  print("No")

"""
B問題_Rotate
"""

a,b,c = map(int, input())
print((a*100 + b*10 + c) + (100*b + 10*c + a) + (100*c + 10*a + b))


"""
C問題_Failing Grade・・・解けた
難易度9
"""

N,P = map(int, input().split())
a = list(map(int, input().split()))
print(sum(1 for i in a if i < P)) 

"""
D問題_Minimize Abs 1・・・解けた（要確認）
難易度118
"""

N,L,R = map(int, input().split())
A = list(map(int, input().split()))
ans = []
x = 0
for a in A:
  # L,Rの範囲で収まるできるだけ少ないXを求める
  if L <= a <= R: x = a
  elif a < L: x = L
  elif R < a: x = R
  ans.append(x)
print(*ans)

"""
E問題_Attraction on Rainy Day・・・解けない
累積和＋動的計画法（典型）
最小値部分和問題の典型
"""


"""
A問題_Spoiler
"""

a,b,c = input().split("|")
print(a + c)


"""
B問題_jogging・・・解けない（要復習）

周期性＋規則性＝数理化アルゴリズム
難易度109

A秒動く→B秒休む
１サイクル＝（A＋B）秒

合計X秒後に動いていた時間を求める

X//（A＋B）・・・何サイクル動いたか？
X％（A＋B）・・・最後に残った部分サイクルの時間（余り時間、最後の未完成サイクルの時間）

完全サイクルで動いた時間＝X // (A＋B）* A

※余り時間では、A秒以内ならそのまま、A秒以上ならA秒だけ動く
未完成サイクルで動いた時間＝ min(A, X % (A + B)) * A


| 処理                    | 意味                   |
| --------------------- | -------------------- |
| `(A + B)`             | 1サイクルの長さ             |
| `X // (A + B)`        | 完全に終わったサイクルの回数       |
| `X % (A + B)`         | 最後に残った部分サイクルの時間      |
| `min(A, X % (A + B))` | 残り時間がA秒より短ければその分だけ動く |

"""

A,B,C,D,E,F,X = map(int, input().split())

def jogging(a, b, c, x):
  """X秒の中で何サイクル分動けるかを計算"""
  period = x // (a + c) # 1周期
  r = x % (a + c) # 次のサイクルの余り時間
  return (period * a + min(a, r)) * b # 総距離（余り時間がa秒未満ならbメートル進む）

t = jogging(A,B,C,X)
a = jogging(D,E,F,X)

if t > a: print("Takahashi") 
elif t < a: print("Aoki")
else: print("Draw")


"""
C問題_Trick Taking・・・解けた
難易度80
"""

from collections import Counter

N,T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
lst = list(zip(C,R))
counter = Counter(C)

def search_mx_idx(p):
  mx = 0; res_i = 0
  for i, (c, r) in enumerate(lst):
    if p == c and mx < r:
      mx = r
      res_i = i + 1
  return res_i

ans = 0
if counter[T] != 0:
  ans = search_mx_idx(T)
else:
  ans = search_mx_idx(C[0])

print(ans)

"""
D問題_Booby Prize・・・解けた
難易度26
"""

N = int(input())
A = list(map(int, input().split()))
B = sorted(A[:])
print(A.index(B[N -2]) + 1)


"""
E問題_Manga・・・土日やる
難易度842
"""


"""
A問題_Lexicographic Order
辞書順の文字列比較
"""

S,T = input().split()
print("Yes" if S < T else "No")

"""
B問題_Water Pressure
"""

D = int(input())
print(D / 100)

"""
C問題_Four Hidden・・・ギリ解けた
難易度79

部分文字列の場所の全探索
部分文字列＝|T|-|U|+1通り

Uの各文字について走査する

”？”はなんでも良い
”？”以外の文字がT＝Uが全て一致しているなら”Yes”
一つでも一致していなければ”No”
"""

T, U = input(), input()
ok = False

# iは開始位置（ループごとに文字が1つずつずれる）
for i in range(len(T) - len(U) + 1): 
  ok = True
  for j in range(len(U)):
    if T[i + j] != "?" and T[i + j] != U[j]:
      ok = False
      break
  if ok:
    print("Yes")
    exit()
print("No")


"""
D問題_Distance Between Tokens・・・解けた
難易度59


２点間の距離を求める（マンハッタン距離）
|x2 - x1| + |y2 - y1| = 2座標の距離
距離を計算する為に座標が必要
H＊W回走査し、S[i][j]が”o”の座標を予め調べておく
"""

H,W = map(int, input().split())
S = [input() for _ in range(H)]

dist = []
for i in range(H):  
  for j in range(W):
    if S[i][j] == "o":
      dist.append((i, j))

x1, y1 = dist[0]
x2, y2 = dist[1]
print(abs(x2 - x1) + abs(y2 - y1))

"""
E問題_Variety Split Easy・・・解けない
難易度184

数列を２つに分割して種類数の合計を最大化する
"""

N = int(input())
A = list(map(int, input().split()))

# 左右のある場所までの種類数を求める
# setを使うことで重複を除き、差分だけが追加される。
st = set()
num_l = [0] * (N + 1)
num_r = [0] * (N + 1)
for i in range(N):
  st.add(A[i])
  num_l[i + 1] = len(st)

st = set()
for i in range(N - 1, -1, -1):
  st.add(A[i])
  num_r[i] =len(st)

ans = 0
for i in range(1, N):
  ans = max(ans, num_l[i] + num_r[i])

print(ans)



"""
A問題_StatusCode
"""

S = int(input())
print("Success" if 200 <= S <= 299 else "Failure")

"""
B問題_Takahashisan2
"""

S = input()
print("Yes" if S[-3:] == "san" else "No")

"""
問題C_Practical Computing・・・解けない
全探索＋組合せ（パスカルの三角形）

問題文の意味を理解する
難易度49
"""

N = int(input())
A = [[0] * N for _ in range(N)]

for i in range(N):
  for j in range(i + 1):
    if j == 0 or j == i:
      A[i][j] = 1
    else:
      A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

for i in range(N):
    for j in range(i + 1):
      if A[i][j] == 0: continue
      print(A[i][j], end=" ")
    print()


"""
問題D_Geometric Sequence・・・解けた
難易度147

等比数列の判定


等比数列は、項 / 前の項＝比が全て同じ（等しい数列）

Ai, Ai + 1, Ai + 2と数列を考える
Ai＋１ / Ai = Ai + 2 / Ai + 1の関係になる
→少数派誤差が出るから移行して整数で計算

Ai*Ai±2=Ai＋１^2

"""

N = int(input())
A = list(map(int, input().split()))
if all(A[i]*A[i + 2] == A[i + 1]**2 for i in range(N - 2)):
  print("Yes")
  exit()

print("No")

"""
E問題_JustK・・・要復習
"""



"""
A問題_Happy New Year 2025
"""

A,B = map(int, input().split())
print((A + B)**2)

"""
B問題_Full House・・・解けた
難易度27
"""

from collections import Counter
A = list(map(int, input().split()))
counter = Counter(A)
ok = True
for val in counter.values():
  if val not in (2, 3):
    ok = False
print("Yes" if ok else "No")


"""
問題C_typo・・・解けた
難易度58

Pythonはリスト同士で等価判定＝＝できる
"""

S = list(input())
T = list(input())

if S == T:
  print("Yes")
  exit()

for i in range(len(S) - 1):
  if S[i] != T[i]:
    S[i], S[i + 1] = S[i + 1], S[i]
    break
if S == T: print("Yes")
else: print("No")


"""
D問題_Go Straight and Turn Right・・・解けた
難易度30
シミュレーション問題
・今の向き
・現在の座標
原点（0,0）から東西南北を進む

向きをmoveの座標で管理
東：０ = x + 1
南：１ = y - 1
西：２ = x - 1
北：３ = y + 1

東＋西＝Xが増減
南＋北＝yが増減

現在位置をcurで管理
"""

N = int(input())
S = input()

x,y = 0, 0
d = 0 # 0:右,1:上,2:左,3:下 
dx = [1, 0,-1, 0]
dy = [0, 1, 0, -1]
for s in S:
  if s == "S":
    x += dx[d]
    y += dy[d]
  else:
    d = (d + 1) % 4
print(x, y)

# 下のコード
N = int(input())
S = input()

x,y = 0, 0
move = 0
for s in S:
  if move % 4 == 0:
    move = 0
  if move == 0 and s == "S":
    x += 1
  elif move == 1 and s == "S":
    y -= 1
  elif move == 2 and s == "S":
    x -= 1
  elif move == 3 and s == "S":
    y += 1
  elif s == "R":
    move += 1
print(x, y)


"""
E問題_One Timme Swap・・・解けない
難易度459

組合せの数え上げ問題
nC2（組合せ）＝ N * (N - 1) // 2
異なるn個の中から2個選ぶ


N 個から 2 個を選ぶとき：

1 個目の選び方 … N 通り

2 個目の選び方 … (N-1) 通り

→ N(N-1) 通りだが「順番を考えると重複する」
（A と B を選ぶのも、B と A を選ぶのも同じ）

だから 2 で割る：


重複ケースの数え上げ

同じ結果を生む操作の分類

全体 - 重複 = 有効なケース数
"""

from collections import Counter

S = input()
N = len(S)

count = Counter(S)

same = 0
# 組合せ(nC2の数え上げ問題:異なるn個の中から2個選ぶ)
comb_all = N * (N - 1) // 2
# スワップした結果
# Sが同じ文字か違う文字かで場合分け
for c in count.values():
  # 同じ文字を入れ替える場合の数
  same += c * (c - 1) // 2
# 違う文字の個数＝nC2 - 同じ文字の個数
# 違う文字同士の入れ替えによって作られる異なる文字列の数
diff = comb_all - same
ans = diff + (1 if same > 0 else 0)
print(ans)


"""
A問題_delete
"""

S = input()
s = S.replace(".", "")
print(s)


"""
B問題_Generalized ABC
"""

K = int(input())
ans = ""
for i in range(K):
  ans += chr(ord("A") + i)
print(ans)


"""
C問題_Distance Table・・・解けた
難易度32

全探索
"""

N = int(input())
D = list(map(int, input().split()))
for i in range(N - 1):
  ans = []
  total = 0
  for j in range(i, N - 1):
    total += D[j]
    ans.append(total)
  print(*ans)

"""
D問題_String Shifting・・・解けない
難易度86
回転操作＋文字列の問題
シフト走査後文字列の辞書順の最小値、最大値を取得

"""

S = input()
N = len(S)
v = []
for k in range(N):
  # 0..N + 0..kでシフト操作を実現している
  # N-1回走査後はシフト前に戻る為、左シフトのみで考えてよい
  v.append(S[k : N] + S[:k])
# ソートではなくmin,maxで文字列の辞書順の最小値・最大値を取得
print(min(v), max(v), sep="\n")



"""
E問題_Count Connected Components・・・もう少しで解ける
グラフ＋BFS
(https://atcoder.jp/contests/abc284/tasks/abc284_c)
連結成分の個数を求める問題
1-2-3 4 5-6
連結成分＝3

{1,2,3}
{4}
{5.6}

連結成分を数えるには
・全頂点に対して未訪問の位置からBFS/DFSを開始し、
 BFS/DFSの開始回数を数える
"""

from collections import deque

N,M = map(int, input().split())
G = [[] for _ in range(N)]
visited_ = [False] * N

for _ in range(M):
  v,u = map(int, input().split())
  v -= 1; u -= 1
  G[v].append(u)
  G[u].append(v)


def bfs(start):
  que = deque([start])
  visited_[start] = True
  while que:
    v = que.popleft()
    for u in G[v]:
      if not visited_[u]:
        visited_[u] = True
        que.append(u)

count = 0
# 全頂点を走査する為のループ
for i in range(N):
  if not visited_[i]:
    bfs(i)
    count += 1
print(count)


"""
A問題_Probably English
"""

N = int(input())
W = input().split()
for w in W:
  if w in ("and", "not", "that", "the", "you"):
    print("Yes")
    exit()
print("No")


"""
B問題_Online Shopping
"""

N,S,K = map(int, input().split())
total = 0
for _ in range(N):
  p,q = map(int, input().split())
  total += p * q

print(total if total >= S else total + K)


"""
C問題_Takahashi's Failure・・・解けた
難易度42
"""

N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

for bi in B:
  if all(A[bi] >= A[i] for i in range(N)):
    print("Yes")
    exit()
print("No")


"""
D問題_Counterclockwise Rotation・・・解けない（要復習）
難易度180
(https://atcoder.jp/contests/adt_easy_20251120_3/tasks/abc259_b)
幾何（三角関数の問題）

必要な知識
・三角比・・・(sinθ, cosθ, tanθ)
・三角関数・・y = sinX y = cosX y = tanX
・ユークリッド距離
・ベクトル

<三角比の考え方>
sinX・斜辺1, 角度Xの直角三角形の高さ
sinX = 斜辺 * sinθ

cosX・斜辺1, 角度Xの直角三角形の底辺の長さ
cosX = 斜辺 * cosθ

tanX・底辺1, 角度Xの直角三角形の高さ
tanX = 底辺 * tanθ

<ユークリッド距離(2点間の距離)>
√(a^2 + b^2)
"""


"""
E問題_Bipartize・・・解けない（要復習）
難易度629
(https://atcoder.jp/contests/adt_easy_20251120_3/tasks/abc427_c)

二部グラフ、連結性
"""

N,M = map(int, input().split())
G = [tuple(map(int, input().split())) for _ in range(M)]

# 色の塗り方を２^N通り試しそれぞれの辺を見て、
# 結んでいる頂点の色が同じ色だった場合、矛盾するため削除カウントを+1
ans = M
for bit in range(1 << N):
  delete_count = 0
  for v, u in G:
    if 1 & (bit >> v) == 1 & (bit >> u):
      delete_count += 1
  ans = min(ans, delete_count)

print(ans)
