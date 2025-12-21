"""
A問題_12435・・・解けた
難易度43
少し難しい
"""

A = list(map(int, input().split()))
count = 0
for i in range(len(A) - 1):
  if A[i + 1] < A[i]:
    count += 1
    A[i], A[i + 1] = A[i + 1], A[i]

if count == 1 and "".join(map(str, A)) == "12345":
  print("Yes")
else:
  print("No")



"""
B問題_Geometric Sequence・・・解けた
難易度147

等比数列とは、A2／A1の項を割った比が等しい数列

A1 A2 A3 A4 A5
A2/A1 = A3/A2 日は等しい
→小数の計算だと誤差が出るため整数に直すと
★A1*A3 = A2^2になる
"""

N = int(input())
A = list(map(int, input().split()))
for i in range(N - 2):
  if A[i]*A[i + 2] != A[i + 1]**2:
    print("No")
    exit()
print("Yes")