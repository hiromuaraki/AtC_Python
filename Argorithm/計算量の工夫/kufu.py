import bisect

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
累積和
先頭からある場所までの総和を求めておく
r - lでlからrまでの差をO(1)で計算

先頭の配列から数列を末尾へX回移動する
開始位置を保持しておき、開始位置がN回回ったら元に戻る

(Si + X) % N → 移動の開始位置
累積和：N+1個の配列を準備し先頭からある場所までの総和事前に計算しておく
"""

"""
A*B+C = N
愚直に考えるとa,b,cを固定しN^3通り試す

⭐️全探索を改善する場合は固定した時の取りうる範囲を考える

C = N - A*Bで求められる
N > A*B つまり0より大きい範囲がCの取りうる範囲
言い換えると
N ≦ A*Bの間繰り返せばいい為、Bも固定する必要はない
(N-1)//Aを数をカウントしていく

N≦10^6
計算量：O(N）
"""

N = int(input())

# 全探索N^3通り
count = 0
for a in range(1, N):
    for b in range(1, N):
        for c in range(1, N):
            if a * b * c == N:
                count += 1
print(count)


# 計算量の工夫１ N^2通り
for a in range(1, N):
    for b in range(1, N):
        # 改善前
        # c = N - a*b
        # if c > 0:
        #     count += 1
        # 改善後
        # a*bの範囲がN以下の場合のみカウントすればいい
        if a*b <= N:
            count += 1
        



# 計算量の工夫２ N 
ans = 0
for a in range(1, N):
    b_count = (N - 1)//a
    ans += b_count
print(ans)
