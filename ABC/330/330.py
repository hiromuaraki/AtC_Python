"""
A問題_ Counting Passes
"""

N,L = map(int, input().split())
A = list(map(int, input().split()))

print(sum(1 for a in A if L <= a ))


"""
B問題_Minimize Abs 1・・・解けない
難易度114

L,Rの範囲内に収まるできるだけ小さいXを求める
範囲外の場合は、LまたはRをずらす
"""

N,L,R = map(int, input().split())
A = list(map(int, input().split()))
ans = [min(R, max(x, L)) for x in A]
print(*ans)

for a in A:
  x = 0
  if L <= a <= R: x = a
  elif a < L: x = L
  else: x = R
  print(x)

# 別解
ans = [min(R, max(x, L)) for x in A]
print(*ans)


