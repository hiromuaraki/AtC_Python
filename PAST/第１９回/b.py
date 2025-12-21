"""
入金と出勤
"""

N = int(input())
A = list(map(int, input().split()))
x, y = 0, 0
for i in range(N - 1):
  if A[i] < A[i + 1]:
    x += A[i + 1] - A[i]
  else:
    y += A[i] - A[i + 1]
print(x, y)