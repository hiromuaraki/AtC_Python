"""
A問題_HappyBirthday・・・解けた
難易度
難しい（式変形あり）

x,y = 100 * 100 = 10000
"""

X,Y,Z = map(int, input().split())

# 数理的解法


# シミュレーション
for i in range(10000):
  if X == Y * Z:
    print("Yes")
    exit()
  X += i; Y += i
print("No")
"""
問題B_Nearest Taller・・・解けた
難易度

なんでこの問題時間内に解ききれないの？
全探索
"""

N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
  ans = -1
  for j in range(i):
    if A[i] < A[j]:
      ans = j + 1
  print(ans)


"""
C問題_1122 Substring 2・・・要復習
難易度
"""