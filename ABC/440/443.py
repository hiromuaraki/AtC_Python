"""
A問題_
"""
print(input() + "s")

"""
B問題_Setsubun
"""

n,k = map(int, input().split())
year = 0
count = 0
while count < k:
  count += n + year
  year += 1
print(year - 1)

"""
C問題_Chokutter Addiction
3Q
(https://atcoder.jp/contests/abc443/tasks/abc443_c)

時間区間の長さの合計を求める
状態変数はできるだけ削る
・chokuttterを最後に開いた時刻

"""

n,t = map(int, input().split())
a = list(map(int, input().split()))

cur = 0 # 開いた時刻を保持
ans = 0 # 時間区間の長さ
for a_i in a:
  if cur <= a_i:
    ans += a_i - cur # 開いていた時間
    cur = a_i + 100 # 次に開く時刻（未来の時刻）

if cur < t:
  ans += t - cur
print(ans)