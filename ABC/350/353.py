"""
A問題_Buildings
"""

N = int(input())
H = list(map(int , input().split()))
for i in range(1, N):
  if H[0] < H[i]:
    print(i + 1)
    exit()
print(-1)


"""
B問題_AtCoder Amusement Park・・・解けた
難易度51
(https://atcoder.jp/contests/abc353/tasks/abc353_b)

持つべき情報
・空席の数
・アトラクションの台数
"""

N,K = map(int, input().split())
A = list(map(int ,input().split()))

k = K; count = 1
for a in A:
  # 空席の数がグループ数より少ない場合はアトラクションをスタートさせる
  # アトラクションに乗るため毎回必ずa人減る
  if k < a:
    k = K
    count += 1
  k -= a

print(count)



"""
C問題_Sigma Problem
難易度795
(https://atcoder.jp/contests/abc353/tasks/abc353_c)

i < jのi, jを全部足す

1. 総和・ペア問題・・・Aiが何回登場するかで考える
2. 条件は単調にできるか？を常に考える
Aj ≧ M - Aiなら右側は単調＝単調性あり＝二分探索できる
3. 問題を段階的に分割する癖をつける
・総和を作るフェーズ
・余った条件で調整するフェーズ

問題の構造化（式変形・分解・単調性認識）

全てのペアの総和を求める
ΣAi * (N - 1)
※N -1 は自分自身を除いた数

このコードはバッグっている為後日修正
"""


N = int(input())
A = list(map(int, input().split()))

A.sort()
LIMIT = 10**8

total = 0
# i,jの組を総和をO(N)で求める
for i in range(N):
  total += A[i] * (N - 1)

ans = 0
for i in range(N):
  ok = N; ng = -1
  target = LIMIT - A[i]
  while ok - ng > 1:  
    mid = (ok + ng) // 2
    if A[mid] >= target:
      ok = mid
    else:
      ng = mid
  ans += max(0, N - ok)
print(total - ans * LIMIT)



# STEP1 全ペア総和の数学的計算だけを練習
# Aiの数列が与えられた時、Σi < j(Ai + Aj)をO(N)で求める
N = int(input())
A = list(map(int, input().split()))

acc = 0
# 2重ループの全ペアの総和をO(N)で計算
for i in range(N):
  # n-1は自分自身を除いている
  acc += A[i] * (N - 1)
print(acc)


# STEP2 単調性から二分探索で j の範囲を取る練習
# 「Aj ≥ X を満たす j の個数」を二分探索で求める関数を書け**
# A = [1, 3, 4, 7, 10] X = 5 → 答えは 2（7, 10）

X = int(input())
N = int(input())
A = list(map(int, input().split()))

# 条件を満たす境界位置の判定関数
def is_ok(j):
  return A[j] >= X

ok = N; ng = -1

# 二分探索は値ではなくindexを動かす
# "条件を満たす境界位置”を高速で特定する手段
while ok - ng > 1:
  # midは配列のインデックスを求めている
  mid = (ok + ng) // 2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid
print("最初の位置:", ok)
print("個数:", N - ok)


"""

"""
N = int(input())
A = list(map(int ,input().split()))
A.sort()
LIMIT = 10**8
# 答え
ans = 0
for i in range(N):
    # i の範囲は [0, N-1]
    # 条件を満たす → もっと右を探したい → ng = mid
    # 条件を満たさない → 左に戻る → ok = mid
    ok = i; ng = N
    while ng - ok > 1:
      # 条件を満たす最大の i を二分探索で探す:
      mid = (ok + ng) // 2
      if A[i] + A[mid] < LIMIT:
        ok = mid # 条件を満たす → 右へ
      else:
        ng = mid # 条件NG → 左へ
    # 見つけたら、その i の分だけ答えに足す
    ans += ok - i
print(ans)











