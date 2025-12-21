"""
A問題_Arithmetic Progression
等差数列
"""

A,B,D = map(int, input().split())
for i in range(A, B + 1, D):
  print(i, end=" ")


"""
B問題_Append・・・解けた
難易度43
"""

Q = int(input())
A = []

for _ in range(Q):
  t,x = list(map(int, input().split()))
  if t == 1:
    A.append(x)
  else:
    print(A[-x])