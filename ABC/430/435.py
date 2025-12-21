"""
A問題_Triangular Number

等差数列
"""

N = int(input())
print(N * (N + 1) // 2)


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


"""
C問題_Domino・・・解けない
難易度2Q

(https://atcoder.jp/contests/abc435/tasks/abc435_c)

現時点でのどのドミノまでが倒れていることが確定しているか
を保持しながら、左から順に倒れるかどうかを判定していく  
"""

# 岩井星人の解法
N = int(input())
A = list(map(int, input().split()))

right = A[0] - 1 # 最初に倒れる範囲

i = 1
while right > 0 and i < N:
    # i番目が倒れる → さらに右に倒せる可能性
    right = max(right, A[i])
    right -= 1
    i += 1
print(i)


# 公式解法
N=int(input())
A=list(map(int,input().split()))

# 座標が crr 未満のドミノは倒れることが確定している
crr = 1
for i in range(N):
  # 座標 i にあるドミノが倒れるかどうか判定
  if i >= crr:
    print(i)
    exit()
  crr=max(crr, i+A[i])

print(N)


