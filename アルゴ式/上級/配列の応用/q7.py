"""
ライフゲーム
(https://algo-method.com/tasks/642rcPn)
"""

# 各マス目について、生きている(黒) → 1, 死んでいる(白) → 0 として管理する
# 現在のマスの情報 now_ij とその周囲の生きているマスの総数 sum_ij の情報から、次のマスを求める関数
# def next_state(now_ij, sum_ij):
#     # 基本的には現在のマス目のまま
#     ret = now_ij

#     # ただし、ルールに記載されているパターンについては、それに従う
#     if now_ij == 0 and sum_ij == 3: ret = 1
#     if now_ij == 1:
#         if sum_ij <= 1 or sum_ij >= 4: ret = 0
#         else: ret = 1

#     # 次の世代のマス目を返す
#     return ret

# n,x = map(int, input().split())
# s = [list(input()) for _ in range(n)]
# d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
# now = [[0] * n for _ in range(n)]
# for i in range(n):
#   for j in range(n):
#     now[i][j] = (1 if s[i][j] == "#" else 0)

# # 時間を1ステップずつ進める＝同じ盤面をX回更新する
# for k in range(x):
#   nex = [[0] * n for _ in range(n)]
#   for i in range(n):
#     for j in range(n):
#       lift_count = 0
#       for p, q in d:
#         di, dy = p + i, q + j
#         if 0 <= di < n and 0 <= dy < n:
#           lift_count += now[di][dy]
#       nex[i][j] = next_state(now[i][j], lift_count)
#   now = nex

# for i in range(n):
#   ans = ""
#   for j in range(n):
#     ans += ("#" if now[i][j] == 1 else ".")
#   print(ans)

n, x = map(int, input().split())
s = [input() for _ in range(n)]

# 初期状態
now = [[1 if c == "#" else 0 for c in row] for row in s]

# 8方向
d = [(-1,-1), (-1,0), (-1,1),
     (0,-1),         (0,1),
     (1,-1),  (1,0), (1,1)]

for _ in range(x):
    nex = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cnt = 0

            # 近傍カウント
            for di, dj in d:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    cnt += now[ni][nj]

            # ルール適用（インライン）
            if now[i][j] == 0:
                if cnt == 3:
                    nex[i][j] = 1
            else:
                if cnt in (2, 3):
                    nex[i][j] = 1
    now = nex

# 出力（高速）
for row in now:
    print("".join('#' if v else '.' for v in row))


