"""
N
∑i 
i=1
"""

N = int(input())
print(sum(i for i in range(1, N + 1)))


"""
R
Σ (2i - 1)^2
i = L
"""

L,R = map(int, input().split())
total = 0
for i in range(L, R + 1):
    total += (2*i -1)**2
print(total)


"""
N-1 M-1
Σ   Σ (Ai + Bj)
i=0 j=0
"""


N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
for i in range(N):
    for j in range(M):
        total += A[i]+B[j]
print(total)


"""
N−1  N
∑    ∑ ij  
i=1  j=i+1
"""

N = int(input())
ans = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        ans += i*j
print(ans)

"""
for 文と Π 計算・・・総積
N−1
∏
i=0
"""

N = int(input())
A = list(map(int, input().split()))
ans = 1
for i in range(N):
    ans *= A[i]
print(ans % 10)