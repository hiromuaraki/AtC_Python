from collections import Counter
from collections import deque
import heapq,sys,bisect

# 再帰処理のオーバーフロー対策（上限数を変更）
sys.setrecursionlimit(10**6)
'''
しりとり
'''

N = int(input())
S = [input() for _ in range(N)]
ok = True
C = set()
for i in range(N-1):
    if S[i] in C:
        ok = False
        break
    C.add(S[i])
    for a,b in zip(S[i][-1], S[i+1][0]):
        if a != b:
            ok = False
            break
        
print('Yes' if ok and S[N-1] not in C else 'No')



'''
言葉の梯子
'''
N,M = map(int, input().split())
S = [input() for _ in range(N)]
ok = True
for i in range(N-1):
    diff_cnt = 0
    for a,b in zip(S[i], S[i+1]):
        if a != b:
            diff_cnt += 1
    
    if diff_cnt > 1 or diff_cnt == 0:
        ok = False
        break
print('Yes' if ok else 'No')


# ------------ランレングス圧縮----------------------

'''
ランレングス圧縮
'''

S = input()
ans = ""

N = len(S)
i = 0
while i < N:
    c = S[i]
    j = i + 1
    while j < N and c == S[j]:
        j += 1
    ans += c + str(j - i)
    i = j

print(ans)

'''
ランレングス圧縮の復元
'''

S = input()
N = len(S)

ans = ""
i = 0
while i < N:
    c = S[i]
    j = i + 1
    while j < N and S[j].isdigit():
        j += 1
    n = int(S[i+1:j])
    ans += c * n
    i = j

print(ans)


# ------------約数・素数・最大公約数----------------------

    
"""
約数のカウント
"""

N,K=map(int, input().split())
ans=[]

for i in range(N, 0, -1):
    count=0
    for j in range(1, N+1):
        if i%j==0: count+=1
    if count==K:
        ans.append(i)

print(len(ans))



"""
素数の個数
"""

N=int(input())
A=list(map(int, input().split()))
p=[]
for n in A:
    count=0
    for j in range(1, n):
        if n%j==0:
            count+=1
    if count == 1:
        p.append(n)
print(len(p))


"""
最大公約数（再帰処理）

ユークリッドの互除法
A％B==0になるまでクリア返し0になったらBを返却
"""

A,B=map(int, input().split())
if A<B:
    A,B=B,A

def gcd(A,B):
    if A%B==0:
        return B
    return gcd(B, A%B)
print(gcd(A,B))

"""
2でも3でも5でも割り切れない数
"""

N=int(input())
ans=0
for i in range(1, N+1):
    if i%2==0:continue
    if i%3==0:continue
    if i%5==0:continue
    ans+=1
print(ans)


# -----------全探索-------------


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


# ------------クエリ----------------------

"""
スタック・・・後入れ先だし
"""

N=int(input())
A=list(map(int, input().split()))
Q=int(input())

for _ in range(Q):
    query=list(map(int, input().split()))
    if query[0]==0:
        A.append(query[1])
    else:
        if A:
            print(A.pop())
        else:
            print("Error")

"""
クエリ
"""

Q=int(input())
A=[3,1,4,1,5,9,2,6,5,3]
for _ in range(Q):
    query=list(map(int, input().split()))
    t=query[0]
    if t==0:
        print(A[query[1]])
    else:
        A[query[1]]=query[2]

"""
未挿入クエリ
"""

N=int(input())
A=list(map(int, input().split()))
Q=int(input())

for _ in range(Q):
    k,v=map(int, input().split())
    if k==0:
        if v < len(A):
            print(A[v])
        else:
            print("Error")
    else:
        A.append(v)



# ------------グリッド--------------


"""
地図の切り取り・・・グリッド
"""

H,W,x,y=map(int, input().split())
S=[list(input()) for _ in range(H)]
x-=1
y-=1
for i in range(3):
    for j in range(3):
        print(S[x+i][y+j], end="")
    print()



"""
縦横十時・・・グリッド
"""

H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
p,q=map(int, input().split())
c=set()

for i in range(W):
    if S[p][i]=="#":
        c.add((p,i))

for j in range(H):
    if S[j][q]=="#":
        c.add((j,q))
print(len(c))




"""
マインスイーパー・・・グリッド
"""

H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
Q=int(input())

for _ in range(Q):
    count=0
    x,y=map(int, input().split())

    for _ in range(1):
        if y != 0 and S[x][y-1]=="#":count+=1 # 左
        if y != W-1 and S[x][y+1]=="#":count+=1 # 右
        if x != 0 and S[x-1][y]=="#":count+=1 # 上
        if x != H-1 and S[x+1][y]=="#":count+=1 # 下
    print(count)


"""
ロボットの移動・・・グリッド
(sx, sy)=(行、列)
難しい
"""

H,W,sx,sy=map(int, input().split())
S=[input() for _ in range(H)]
N=int(input())
T=input()

for move in T:
    if move=="L" and sy>0 and S[sx][sy-1]==".":sy-=1
    if move=="R" and sy+1<W and S[sx][sy+1]==".":sy+=1
    if move=="U" and sx>0 and S[sx-1][sy]==".":sx-=1
    if move=="D" and sx+1<H and S[sx+1][sy]==".":sx+=1

print(sx,sy)

# ------------ソート----------------


"""
バブルソート
計算量：O(N^2)

隣同士の並べ替え（昇順）

隣接する２つの要素の大きさが逆転していたら並べ替える
並べ替えの過程を出力
"""

N=int(input())
A=list(map(int, input().split()))

for _ in range(N):
    is_swap=False
    for j in range(N-1):
        if A[j+1] < A[j]:
            A[j],A[j+1]=A[j+1],A[j]
            is_swap=True
    if is_swap:
        print(*A)
    else:
        break

"""
選択ソート・・・理解不足

計算量：O(N^2)

配列から最小の要素を取り出すことを繰り返す
最小の要素の位置
検索範囲をk+1ずつ減らしていく

5

2 1 3 4 1 = 1

k=0
1 2 3 4 1

k=1
2 3 4 1 = 1

1 1 3 4 2
"""

N=int(input())
A=list(map(int, input().split()))

for k in range(N-1):
  min_idx = A[k:].index(min(A[k:])) + k
  A[k],A[min_idx] = A[min_idx], A[k]
  print(*A)



"""
挿入ソート
計算量：O(N^2)

昇順にソートされた配列の適切な位置に要素を挿入すると、挿入後の配列もまた昇順にソートされている。
"""


N=int(input())
A=list(map(int, input().split()))

for k in range(1, N):
    pos=k
    while pos!=0 and A[pos-1] > A[pos]:
        A[pos-1],A[pos]=A[pos],A[pos-1]
        pos-=1
    print(*A)


"""
バケットソート・・・難しい
計算量：O(N+Akind)？

＝累積和を使った座席割り当て

座る場所の位置を累積和で事前に計算
・各数字の登場回数（頻度分布）
・各数字の総数


要素同士の値を比較しないソートである
要素を取り出すためのN個分のバケツを用意

5
2 1 3 4 1

1:2
2:1
3:1
4:1

各要素数を配列に記録
[0,2,1,1,1]
"""

N=int(input())
A=list(map(int, input().split()))
X=N+1

num=[0]*X
# 各要素を数える（頻度分布）
# 数字xが何回出てくるか
for a in A:
    num[a]+=1

# 並べる位置を決める（累積和）
# 「0 〜 x までに出てきた数字の総数」
# 各数字が「並べ替えたリストでどこから始まるか」を計算
# acc[x] = 「数字 x までに、全部で何個の数字が出てきたか」
# 数字の置き場所を前もって決める
acc=[0]*X
for x in range(N):
    if x==0: acc[x]=num[x]
    else:acc[x]=acc[x-1]+num[x]

B=[0]*N
for a in A:
    acc[a]-=1
    B[acc[a]]=a

print(*B)

"""
中央値
"""

N=int(input())
A=list(map(int, input().split()))
A.sort()
if N%2!=0:
    print(A[N//2])
else:
    n=sum(A[(N//2)-1:(N//2)+1])
    print(n/2)

"""
X番目に小さい数
"""

N,M=map(int, input().split())
A=list(map(int, input().split()))
X=list(map(int, input().split()))
A.sort()

for x in X:
    print(A[x])

"""
総和の最大値
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))
print(sum(sorted(A, reverse=True)[:K]))


"""
差の最小値・・・難しい（要復習）
計算量：O(N log N)

連続 K 個を見れば「その K 個の最大−最小」が簡単に求まる
最小差＝ソート後の連続 K 個

N-K＋1＝連続してK個を取れる総数（取り方の数）
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))
best=float("inf")
A.sort()
for i in range(N-K+1):
    diff=A[i+K-1]-A[i]
    if diff < best:
        best=diff
print(best)

"""
在庫付き最小コスト購入・・・難しい

安いものから順に買っていく→先に（価格、在庫）のペアを価格で昇順にする
[(2,1),(4,3),(6,5)]
"""

N,K=map(int, input().split())
items=[tuple(map(int, input().split())) for _ in range(N)]
items.sort(key=lambda p: p[0])

need,cost=K,0
for price,stock in items:
    buy=min(stock, need)
    cost+=price*buy
    need -= buy
    
    if need == 0:
        break
print(cost)

"""
文字数の種類
"""

N=int(input())
S=set(input().split())
print(len(S))


"""
文字列に現れない文字
"""

S=set(input())
D=set(chr(ord("a")+i) for i in range(26))
print(len(D-S))


"""
注文
"""

N,M=map(int, input().split())
menu={}
for _ in range(N):
    f_,price=input().split()
    menu[f_]=int(price)
X=input().split()

total=0
for x in X:
    total+=menu[x]
print(total)


"""
最頻文字列

まず出現回数が多い順に並べる
出現回数が同じ場合は、文字列を辞書順で並べる

条件：
1. 出現回数の多い順＝-item[1]
2. 回数が同じ場合は、文字列の辞書順
"""

N=input()
S=input().split()
count=Counter(S)
ans=sorted(
    count.items(),
    key=lambda item: (-item[1], item[0]))
print(ans[0][0])

# --------------------総和----------------------

"""
ダーツ・・・全探索
計算量：O(N^3)

各プレイの得点の合計値としてありうるものは何通りか。
３重ループし得点を辞書で辞書で管理


【N^3通り】
[0,2,4]
i=0 j=0 k=0..2
(0,0,0)=0
(0,0,2)=2
(0,0,4)=4

i=0 j=1 k=0..2
(0,2,0)=2
(0,2,2)=4
(0,2,4)=6

i=0 j=2 k=0..2
(0,4,0)=4
(0,4,2)=6
(0,4,4)=8

i=1 j=0 k=0..2
(2,0,0)=2
(2,0,2)=4
(2,0,4)=6

i=1 j=1 k=0..2
(2,2,0)=4
(2,2,2)=6
(2,2,4)=8

i=1 j=2 k=0..2
(2,4,0)=6
(2,4,2)=8
(2,4,4)=10

i=2 j=0 k=0..2
(2,4,0)=6
(2,4,2)=8
(2,4,4)=10

.....
"""

N=int(input())
A=[0]+list(map(int, input().split()))

count={}
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            score=A[i]+A[j]+A[k]
            count[score]=1

print(len(count))


"""
distinctにせよ
数列が互いに相違なる状態（違う）

Counter(A)

3 1 4 1 5
A={3:1, 1:2, 4:1, 5:1}
"""

N=int(input())
A=list(map(int, input().split()))
counter = Counter(A)

print(sum(cnt-1 for cnt in counter.values()))

"""
部分集合を作る・・・解けなかった
最小削除数を求める
難しい

"""
from collections import Counter
N=int(input())
A=list(map(int, input().split()))
counter=Counter(A)

remove_count = 0
for v, cnt in counter.items():
    if cnt >= v:
        remove_count += cnt - v
    else:
        remove_count += cnt

print(remove_count)

"""
1からNまでの総和
"""

# --------------------再帰処理----------------------

N=int(input())


def func0(x):
    if x==0:
        return 0
    return x + func0(x-1)
print(func0(N))

# 別解(等差数列)
print((1+N)*N//2)

"""
AからBまでの整数の総和
"""

import sys

A,B=map(int, input().split())

def func1(a, n):
    if n < a:
        return 0
    return n + func1(a, n-1)

print(func1(A,B))

# 別解（累積和）
print(sum(i for i in range(A,B+1)))

"""
N!!(Nの二重階乗)
N*(N-2)の累積和

"""

N=int(input())

def func(n):
    if n < 3:
        return n
    return n * func(n-2)

print(func(N))

# 別解
ans=1
for i in range(N, 0, -2):
    ans*=i
print(ans)


"""
回文
"""

N=int(input())
X=input()
S=X[0]

for i in range(1,N):
    S=S+X[i]+S
print(S) 

# 再帰処理

def build(i,x):
    if i==0:
        return X[0]
    prev = build(i - 1, X)
    return prev + X[i] + prev

print(build(N-1, X))


# --------------------グラフ----------------------
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


# --------------------計算量の工夫(累積和)----------------------

"""
差の最大値
昇順に並べ替え末尾(最大)-先頭(最小)を行う方針
最大値と最小値を取得し差を求める方針
"""

N=int(input())
A=list(map(int, input().split()))
A.sort()
print(A[-1]-A[0])

# 別解
mx=max(A)
mn=min(A)
print(mx-mn)


"""
1 個除外した総和の最大値
"""

N=int(input())
A=list(map(int, input().split()))
print(sum(A)-min(A))


"""
3つの数の和（計算量の工夫）・・・解けない
min,maxの概念を理解する

O(N^3)通り→0(N^2)通りにする

x,yの値が決まればzの取りうる範囲が決まる

x+y+z=M
z=M-x-y

ここまではわかった。数式化も求めた

ここが解けなかった

zの取りうる範囲の求め方：
min(N, M-x-y)

"""

N,M=map(int, input().split())

ans=0
for x in range(1,N+1):
    for y in range(1,N+1):
        # zの取りうる範囲を計算
        min_z=min(N, M-x-y)
        # x,yがMを超えている場合は対象外
        if min_z<=0:
            continue
        ans+=min_z
        
print(ans)

"""
積の総和 (1)

総和の2乗 = 各要素の積を全部並べて足したもの
分配法則の性質
"""

N=int(input())
A=list(map(int, input().split()))
print(sum(A)**2)


"""
積の総和（２）・・・解けない
和の2乗に注目
S^2=(A0+A1+A2+A3..AN-1)^2

全体の和の2乗 − 各自の二乗
和の2乗から二乗和を引く
"""

N=int(input())
A=list(map(int, input().split()))

S1=sum(A)
S2=sum(x*x for x in A)
ans=(S1*S1-S2)//2
print(ans)


"""
和の総和（基礎編）・・・解けた

数列A=[1,2,3]を[a,b,c]と考える。
(a+b+c)^2となり、
Aの総和の2乗は6=6^2=36
N回計算している為、Aの総和の2乗//N（数列の要素数）から求める。
入力：
N=3
A=[1,2,3]なので

36//3=12
"""


N=int(input())
A=list(map(int, input().split()))

S=sum(A)
print(S*S//N)

"""
② 差の総和・・・解けない
"""




"""
総和クエリ (1)
計算量：O(N＋Q)
前計算として範囲の和を求めておく手法＝累積和

acc[k+1]=acc[k]+A k
"""

# 累積和で前計算（予め総和を計算しておく）
# acc[k]: 左から k 個分の総和
N=int(input())
A=list(map(int, input().split()))
# N+1個の累積和用の配列を用意
acc=[0]*(N+1)

for i in range(N):
    acc[i+1]=acc[i]+A[i]

Q=int(input())
for _ in range(Q):
    k=int(input())
    print(acc[k])


"""
総和クエリ(2)・・・・累積和
計算量：O(N＋Q）

l,rより距離を求める
A=[1,2,3,4,5]

acc=[0,0,0,0,0,0]

前計算で作るアルゴリズム
acc=[0,1,3,6,10,15]

距離を求める
R-L=[l,r]距離

数列の左端からk個の総和を求める

Sl-Sr=Sk
"""

N=int(input())
A=list(map(int, input().split()))
acc=[0]*(N+1)
for i in range(N):
    acc[i+1]=acc[i]+A[i]

Q=int(input())
for _ in range(Q):
    l,r=map(int, input().split())
    print(acc[r]-acc[l])


"""
繁忙期・・・解けない

計算量：O(N）

難しい
連続D日間の最も多い来場者数の期間を求める
"""

N,D=map(int, input().split())
X=list(map(int, input().split()))
acc=[0]*(N+1)

# 日 0 から 日 i より前までの合計来場者数
for i in range(N):
    acc[i+1]=acc[i]+X[i]

# 開始日、最大の来場者数を準備
max_start, max_visitor=0,0

for i in range(N-D+1):
    preriod_visitor=acc[i+D]-acc[i]
    if preriod_visitor >= max_visitor:
        max_start = i
        max_visitor = preriod_visitor
max_end = max_start+D-1
print(max_start, max_end, sep="~")


"""
駅と駅の距離・・・解けた

計算量：O(N＋Q）
右端ー左端＝区間の距離

r-l＝区間の距離
r=右端（最大値）
l=左端（最小値）
"""

N=int(input())
d=list(map(int, input().split()))
acc=[0]*(N+1)

# 区間iからN-1までの累積和を計算
for i in range(N-1):
    acc[i+1]=acc[i]+d[i]

Q=int(input())
for _ in range(Q):
    l,r=map(int, input().split())
    print(acc[r]-acc[l])



"""
ひもの本数・・・・解けない（愚直解は解けた）
ソート＋二分探索あるいはソート＋累積和
難しい
計算量：O(N log N + Q log N)
binsectは境界を探すので、left==rightに収束して終わる
"""

# 計算量を意識した解法
# 二分探索法でA以上B以下の最初に登場する位置と最後に登場する次の位置のidxを取得
# right-leftで求める
N=int(input())
L=list(map(int, input().split()))
L.sort()

Q=int(input())
for _ in range(N):
    A,B=map(int, input().split())
    left=bisect.bisect_left(L,A) # A以上の最初の位置を探す
    right=bisect.bisect_right(L,B) # B以下の最後の位置の次を探す
    print(right-left)

# 計算量を意識しない場合の解法


for _ in range(Q):
    count=0
    A,B=map(int, input().split())
    for i in range(N):
        if A<=L[i]<=B:
            count+=1
    print(count)


# -----------代表的なデータ構造---------------------
"""
ハッシュ
計算量：O(Q)

文字列をキーにし出現回数を数える
※重複は除れる、存在しないキーにアクセスした場合値は０が還る為、エラーにならない

"""
N=int(input())
S=list(input().split())
hash=Counter(S)

Q=int(input())
for _ in range(Q):
    T=input()
    print(hash[T])


# ------------二分探索--------------------
"""
方程式を解く・・・解けない
0以上100以下の実数xを求める
先頭＝０
末尾＝１００

中点＝（先頭＋末尾）/２

方程式：
x(x(x+1)+2)+3==N


条件を満たすXの範囲を絞る
1e4=10^-4=0.00001
"""

N=float(input())
left=0
right=100

def f(x):
    return x*(x*(x+1)+2)+3

while (right-left>1e-4):
    mid=(left+right)/2
    if f(mid)<N:
        left=mid
    else:
        right=mid
ans=left
print(ans)


"""
計算量：O(log N)

二分法
Yes /Noで答えらえる
ある地点までYes、ある地点からNo
2
1,2,3,4,5

データを予め昇順にしておく
"""

X=int(input())
A=list(map(int, input().split()))

left, right = 0, len(A)
idx=-1

A.sort()

while left<right:
  mid=(left+right)//2
  if A[mid]==X:
    idx=mid
    break
  elif A[mid] > X:
    # 探索範囲を左へ
    right=mid-1
  else:
    # 探索範囲を右へ
    left=mid+1

if idx!=-1:
  print(f"{X}のインデックは{idx}")
else:
  print("検索データが見つかりません。")


"""
二分探索
最終的な答えはleft＝rightとなる
"""

# bisectモジュールを使った二分探索
# A[x]>=B[i]のインんデックスを取得
N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

for b in B:
    k=bisect.bisect_left(A, b)
    print(k)

# 別解（自分で書く）
for i in range(M):
    left=0
    right=N
    while left!=right:
        mid=(left+right)//2
        if A[mid]>=B[i]:
            right=mid
        else:
            left=mid+1
    print(left)


# 全探索 0(MN)
for b in B:
    idx=-1
    for x in range(N):
        if A[x]>=b:
            idx=x
            break
    print(idx)


"""
データを予め昇順にする
"""

N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()

for i in range(M):
    left=0
    right=N
    while left!=right:
        mid=(left+right)//2
        if A[mid]>B[i]:
            right=mid
        else:
            left=mid+1
    print(left)

"""
和がK以上のペア
i+j=K
j=K-i

i,kは固定
A[mid]>=K-A[i]
"""

N,K=map(int, input().split())
A=list(map(int, input().split()))

A.sort()
count=0
for i in range(N):
    left=0
    right=N
    while left!=right:
        mid=(left+right)//2
        if A[mid]>=K-A[i]:
            right=mid
        else:
            left=mid+1
    count+=N-left
print(count)