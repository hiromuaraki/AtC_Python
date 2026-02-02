"""
B問題_Mongeness
diff81
機械的に解く。
(https://atcoder.jp/contests/abc224/tasks/abc224_b)
Monge性（行列問題＋全探索）
隣り合う要素の和が特定の関係を満たす性質

左上＋右下≦ 左下＋右上の不等式が成り立つ性質
対角線＋逆対角線の和の合計

Aij + Ai+1,j+1 ≦ Ai,j+1 + Ai + 1,j

(i1, i2, j1, j2)の全ての組みを全探索する
N <= 50 O(N^4)

局所条件（隣接2×2）だけで十分

"""
h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

# O(N^2)
for i in range(h - 1):
  for j in range(w - 1):
    # 左上＋右下 ≦ 右上 + 左下 = 対角線 ≦ 逆対角線の和
    if not (a[i][j] + a[i + 1][j + 1] <= a[i][j + 1] + a[i + 1][j]):
      print("No")
      exit()
print("Yes")

# 全探索 O(N^4)
# for i1 in range(h): # 0〜h-1
#   for i2 in range(i1): # 0-i1-1
#     for j1 in range(w): # 0〜w-1
#       for j2 in range(j1): #0〜j1-1 
#         if not (a[i1][j1] + a[i2][j2] <= a[i2][j1] + a[i1][j2]):
#           print("No")
#           exit()
# print("Yes")



