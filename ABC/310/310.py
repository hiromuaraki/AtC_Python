"""
A問題_Order Something Else・・・解けた
難易度23
"""

N,P,Q = map(int, input().split())
D = list(map(int, input().split()))
ans = P
for d in D:
  ans = min(ans, Q + d)
print(ans)


"""
価格比較（≤ / < / =）
機能比較（⊆ / ⊂）
組み合わせ条件（両方をAND）
安い or 同価格で機能が上
"""


N,M = map(int, input().split())

P,C, F = [],[],[]
for _ in range(N):
  lst = list(map(int, input().split()))
  P.append(lst[0])
  C.append(lst[1])
  F.append(set(lst[2:]))

for i in range(N):
  for j in range(N):
    if i == j: continue
    # iはjの機能を全て持っている
    if F[j] <= F[i]: # j ⊆ i
      # (1) i の方が高い場合または# (2) 同じ価格でも、i が余分な機能を持つ場合
      if P[i] < P[j] or (P[i] == P[j] and F[i] > F[j]):
        print("Yes")
        exit()

print("No")

