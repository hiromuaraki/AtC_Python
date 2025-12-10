import bisect

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


N,Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N):
  S[i + 1] = S[i] + A[i]

si = 0
for _ in range(Q):
  query = list(map(int, input().split()))
  t = query[0]
  if t == 1:
    c = query[1]
    si = (si + c) % N

  else:
    l, r = query[1:]
    l -= 1; r -= 1
    l = (l + si) % N
    r = (r + si) % N
    ans = 0
    if l <= r:
      ans = S[r + 1] - S[l]
    else:
      ans = S[N] - (S[l] - S[r + 1])
    print(ans)
    

"""
区間の総和

計算しやすい形に整える
事前に前計算しR-L−１ O(1)で求める

"""

N = int(input())
S1 = [0] * (N + 1)
S2 = [0] * (N + 1)
for i in range(N):
  c,p = map(int, input().split())
  if c == 1:
    S1[i + 1] = S1[i] + p
    S2[i + 1] = S2[i]
  else:
    S2[i + 1] = S2[i] + p
    S1[i + 1] = S1[i]

Q = int(input())
for _ in range(Q):
  L,R = map(int, input().split())
  print(S1[R] - S1[L - 1], S2[R] - S2[L - 1])
