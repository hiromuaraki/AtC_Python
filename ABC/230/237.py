"""
B問題_Matrix Transposition
(https://atcoder.jp/contests/abc237/tasks/abc237_b)
転置行列
   0 1 2
0: 1 2 3
1: 4 5 6
2: 7 8 9
3: 10 11 12

1 4 7 10
2 5 8 11
3 6 9 12


(0,0),(1,0),(2,0),(3,0)
(0,1),(1,1),(2,1),(3,1)
(0,2),(1,2),(2,2),(3,2)

[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

"""

h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

# 標準
for j in range(w):
  for i in range(h):
    print(a[i][j], end=" ")
  print()

# 別解
for row in zip(*a):
  print(*row)