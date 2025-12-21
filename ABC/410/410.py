"""
問題A_G1
"""

N = int(input())
A = list(map(int, input().split()))
K = int(input())
print(sum(1 for i in range(N) if K <= A[i]))



"""
B問題_Reverse Proxy・・・解けた
難易度57
"""

N,Q = map(int, input().split())
X = list(map(int, input().split()))
A = [0] * N
ans = []
for x in X:
  if x == 0:
    x = A.index(min(A)) + 1
  A[x - 1] += 1
  ans.append(x)
print(*ans)