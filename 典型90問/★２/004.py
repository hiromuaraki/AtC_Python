"""
【グリッドの問題・・・包除原理（前計算）】
扱いやすい形にして前計算

和集合A、和集合Bのように重複したところを足したり引いたりすることを
包除原理という
i行目の合計＋j列目の合計-(i, j)マスの値＝クロスの合計 

グリッドの縦計算

row[j] += A[i][j]
＊＊row[j] += が肝
i = 0開始時は横列を並べるイメージ
jのインデックスは＋１ずづ動的に変化していくから
row[j] +=しておくことで前計算を再利用しているロジック

以降は前の累積和が順にrow[j] = row[j]（縦） + A[i][j]（横）の値で加算されていき
縦の総和になる
"""

H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
row = [0] * (H + 1)
column = [0] * (W + 1)

for i in range(H):
  for j in range(W):
    # 縦と横の合計を事前に求めておく
    row[i] += A[i][j]
    column[j] += A[i][j]

for i in range(H):
  ans = []
  for j in range(W):
    ans.append(column[j] + row[i] - A[i][j])
  print(*ans)


# 他の人の解法
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sum = [sum(A[i]) for i in range(H)]
col_sum = [sum(A[i][j] for i in range(H)) for j in range(W)]

B = [[row_sum[i] + col_sum[j] - A[i][j] for j in range(W)] for i in range(H)]

for row in B:
    print(*row)