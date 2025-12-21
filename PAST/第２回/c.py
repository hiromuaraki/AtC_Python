"""
山崩し・・・自力AC
難しい
"""

N=int(input())
T=[list(input()) for _ in range(N)]

for i in range(N-2, -1, -1):
  for j in range(1, 2*N-1):
    if T[i][j]=="#":
      # 左下
      if T[i+1][j-1]=="X":
        T[i][j]="X"
      # 真下
      if T[i+1][j]=="X":
        T[i][j]="X"
      # 右下
      if T[i+1][j+1]=="X":
        T[i][j]="X"
  
for i in range(N):
  print("".join(T[i]))