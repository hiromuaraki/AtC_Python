import bisect


"""
基本的な二分探索の型

ある地点まではOK, ある地点からはNGに切り替わる最小または最大の境界(index)を探す
OK／NGに２択Yes,NO判定問題にできるなら、単調性あり＝二分探索できる
つまりOK,NGは単調に切り替わる境界（インデックス）探す役割
その開始と終了までの範囲

必ず事前にソートしておく

is_ok関数は「なにを満たすか？」だけ返す
midはindex

① ok / ng の意味
ok … 条件を満たす最後に分かっている index（または「条件を満たす側の境界」）
ng … 条件を満たさない最後に分かっている index（または「条件を満たさない側の境界」）

② ok - ng > 1 の意図 = 未探索の領域が無くなるまで＝ok,ngが隣りあったら探索終了
ok と ng の間には まだ調べていない index がある
差が 1 になると、間に未探索の index はなくなる
つまり ok と ng が隣り合った状態になると探索終了

言い換えると：
ok と ng の間に探索対象がなくなったら、これ以上探索する必要はない
"""

A = list(map(int, input().split()))
A.sort() # 単調性（単調増加する）
N = len(A)
X = 5  # 例

# ---------- 最小 index を求める ----------
# 境界の外側に置く → 例: ok=N, ng=-1
ok_min = N    # 条件を満たす最初の index
ng_min = -1   # 条件を満たさない位置

def is_ok(mid):
    return A[mid] >= X

while ok_min - ng_min > 1:
    mid = (ok_min + ng_min) // 2
    if is_ok(mid):
        ok_min = mid   # 条件を満たす → 左端に寄せるため ok を mid に
    else:
        ng_min = mid   # 条件を満たさない → ng を mid に

# ---------- 最大 index を求める ----------
ok_max = -1   # 条件を満たす最後の index
ng_max = N    # 条件を満たさない位置

while ng_max - ok_max > 1:
    mid = (ok_max + ng_max) // 2
    if is_ok(mid):
        ok_max = mid   # 条件を満たす → 右端に寄せる
    else:
        ng_max = mid   # 条件を満たさない → 左に戻す

print("最小 index:", ok_min)
print("最大 index:", ok_max)



"""
計算量：O(N log N）

二分探索の練習とおさらい
OK:条件を満たす可能性がある最も右
NG:条件を満た差ない可能性がある最も左
＝境界の外側

最小も最大も、okに常に答えが入る＝OKが常に答え側

最小インデックス探索（OK側が右）
NG NG NG NG | OK OK OK ...
            ↑答え（最初のOK）


最大インデックス探索（OK側が左）
... OK OK OK | NG NG NG
      ↑答え（最後のOK）
"""


N,X = map(int, input().split())
A = list(map(int, input().split()))

# 昇順にソートしないと単調増加しない＝単調性にならない為、二分探索できない
A.sort()

def is_ok(mid):
  return A[mid] >= X

ok = N; ng = -1 # ok,ngには条件を満たす／満たさない範囲外の値を設定
while ok - ng > 1:
  # Ai ≧ Xを満たす最小のインデックスを求める
  mid = (ok + ng) // 2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
# -1: 最小のインデックスなし/ -1以外: 最小のインデックスあり
print(-1 if ok == N else ok)

# Ai ≧ Xを満たす最大のインデックスを求める
ok = -1; ng = N # ok,ngには条件を満たす／満たさない範囲外の値を設定
while ng - ok > 1:
  mid = (ng + ok) // 2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
print(ok)






"""
典型アルゴリズム問題集A
計算量：O(log N）

Ai≧Kとなるインデックスの最小のインデックスを求める
K以下となる最小の最大のインデックスは存在するか？
Yes／No

単調性＝二分探索
"""


N,K = map(int, input().split())
A = list(map(int, input().split()))

left = 0 # 下限値を設定
right = N  # 上限値を設定

while (right - left > 1): # 探索行ほが1つになるまで繰り返す
  mid = (left + right) // 2 # 探索行ほを絞る
  if A[mid] < K:
    left = mid
  else:
    right = mid

left += 1 # 1-indexedに調整
print(left if left != N else -1)

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
Ax<=Bkを満たす個数
予めデータを昇順にする

計算量：O(M lgo N)
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

# 別解
import bisect

N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()

for b in B:
    print(bisect.bisect_right(A, b))


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


"""
最小の添え字
"""

# TLE
N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    idx = 0
    for i in range(N):
        if A[i] < b:
            idx = i + 1
    print(idx)


"""
段階評価

Ai≧Kであるインデックスiのうち、
最小のものを求める
"""

import bisect

N,K = map(int, input().split())
A = list(map(int, input().split())) 
X = list(map(int, input().split()))

for a in A:
    print(bisect.bisect_right(X, a))


# 地力解法
N,K = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

for a in A:
    left = 0 # 下限値を設定
    right = K # 上限値を設定
    while left != right:
        mid = (left + right) // 2
        if X[mid] <= a:
            left = mid + 1 # OKならleftの探索範囲を右側に狭める
        else:
            right = mid # NGなら探索範囲を左側に狭める
    print(left)


"""
ひもを切る

left = 0 常に条件を満たす確実な値＝OK
right = 10++5 常に条件を満たさない確実な値＝NG

最終的な答え：left
"""

N,K = map(int, input().split())
L = list(map(float, input().split()))

def f(x, L):
    ans = 0
    for l in L:
        # 長さLのひもを切る処理
        ans += int(l/x)        
    return ans

ans = 0
left = 0 # 常に条件を満たすOK
right = 10**5 # 常に条件を満たさないNG
while (right - left > 1e-8):
  mid = (left + right) / 2
  if f(mid, L) >= K:
    left = mid
  else:
    right = mid
print(left)


"""
C問題_146_Buy an Integer

所持金Xで買うことのできる最大整数を求める

x円で買える最大の領域を調べる
=最大のOKを求める設計
"""

A,B,X = map(int, input().split())

left = 0 # 常に条件を満たす値
right = (10**9)+1# 常に条件を満たさない値

while (right - left > 1): # 探索領域が1つになるまで繰り返す
  mid = (left + right) // 2
  d = len(str(mid)) # 桁数を取得
  price = A*mid + B*d
  if price <= X:
    left = mid
  else:
    right = mid
print(left)

"""
99の表（１）
N＊Nの表の中にK以下はいくつあるか？

(i + 1) * (j + 1) ≦ Kを満たす
0 ≦ j ≦ N - 1のjはいくつあるか？

j ≦ K // (i + 1) - 1
min(N, K // (i + 1))
"""

N,K = map(int, input().split())
ans = 0
for i in range(N):
    ans += min(N, K // (i + 1))
print(ans)


"""
99の表（２）

ある数K以下が何個あるか？
"""

N,X = map(int, input().split())
left = 1
right = N * N

# f(K) を求める関数
def f(N,K):
    count = 0
    for i in range(N):
        count += min(N, K//(i+1))
    return count

while left != right:
    mid = (left + right) // 2
    if f(N, mid) >= X:
        right = mid
    else:
        left = mid + 1
print(left)
