"""
A問題_Candy Cookie Law
"""

A,B,C,D = map(int, input().split())
if C >= A and D < B: print("Yes")
else: print("No")


"""
B問題_CountSubgrid・・・解けない
難易度141

グリッド操作
"""

N,M = map(int, input().split())
S = [input() for _ in range(N)]

st = set()
for i in range(N - M + 1):
  for j in range(N - M + 1):
    # M*Mの領域を取り出す
    sub = []
    for k in range(M):
      sub.append(S[i + k][j : j + M])
    st.add(tuple(sub))

print(len(st))


"""
C問題_・・・要復習
"""

N, A, B = map(int, input().split())
S = input().strip()

# 累積和
S_a = [0] * (N + 1)
S_b = [0] * (N + 1)
for i in range(N):
    S_a[i + 1] = S_a[i] + (S[i] == 'a')
    S_b[i + 1] = S_b[i] + (S[i] == 'b')

ans = 0
l1 = 0  # a の条件を満たすための左端
l2 = 0  # b の条件を満たすための左端

for r in range(1, N + 1):
    # a が A 以上になるように l1 を進める
    while l1 < r and S_a[r] - S_a[l1] >= A:
        l1 += 1
    # b が B 未満を満たさなくなるまで l2 を進める
    while l2 < r and S_b[r] - S_b[l2] >= B:
        l2 += 1

    # 区間 [L, R] で条件を満たす L の個数は？
    # a条件を満たすLは l1-1 以前、b条件を満たすLは l2 以降
    # → [l2, l1-1] の範囲
    if l2 < l1:
        ans += (l1 - l2)

print(ans)
