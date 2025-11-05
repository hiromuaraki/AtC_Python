"""
【偶奇性（パリティ）】


ちょうどK回の操作でA＝Bにできるか？
Aを−１、または＋１する

規則性
＋１、−１するごとに偶奇が交互に入れ替わる

Kが偶数ならばAとBの偶奇が同じ
Kが奇数ならばAとBの偶奇が異なる

OK：両方とも偶数または奇数
0 = 0
1 = 1

NG：偶奇が一致しない
1 ≠ 0
0 ≠ 1

"""

N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
ok = True
for i in range(N):
  diff += abs(A[i] - B[i])
  if diff > K:
    ok = False
    break

if diff % 2 != K % 2:
  ok = False

print("Yes" if ok else "No")
