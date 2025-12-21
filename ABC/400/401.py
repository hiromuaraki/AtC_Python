"""
A問題_StatusCode
"""

S = int(input())
print("Success" if 200 <= S <= 299 else "Failure")


"""
B問題_Unauthorized・・・解けた
難易度20

シミュレーション
"""

N = int(input())
is_login = False
ans = 0
for _ in range(N):
  S = input()
  if S == "login":
    is_login = True
  elif S == "logout":
    is_login = False
  elif S == "private" and not is_login:
    ans += 1
print(ans)


"""
C問題_K-bonacci・・・解けない
難易度284
(https://atcoder.jp/contests/abc401/tasks/abc401_c)
累積和の問題

累積和・・・ある場所からある場所までの区間の和
区間和は累積和を使う

フィボナッチ数列
f(n) = f(n - 1) + f(n - 2)
=前の２個の和が次の項

K..N + 1までの範囲を累積和
A = [1] * K →Kの1で初期化済みの配列を作成

S = 前２個の和

10**9 = 10^9 = 1_000_000_000
%（MOD）
例）75 % 10 = （7あまり）5 → 75ー10*７

"""

N,K = map(int, input().split())
# N+1個の1で初期化済みの配列を作る
A = [1] * (N + 1)

S = K # S：前2個の和を更新する変数
MOD = 10**9
# 累積和
# iはKから開始する為、i < Kの場合分けが不要
for i in range(K, N + 1):
  A[i] = S
  S += S - A[i - K]
  # 基本10**9を超えなためSは変化しない
  # 最後に％すると値が大きくなり計算に時間がかかるので、都度％し値を小さくしておく（Sが10**9以上の場合）
  S %= MOD
print(A[N])