"""
迷路
(https://algo-method.com/tasks/424)
コマがマス(X1, Y1)にたどり着く最小移動距離
"""
H,W = map(int, input().split())
X0,Y0,X1,Y1 = map(int, input().split()) # 盤上のコマの始点と終点
S = [input() for _ in range(H)] # コマの状態
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 上下左右の座標のチェック用配列タプル
dist = [[-1] * W for _ in range(H)] # マス(i, j)まで移動距離を管理する配列

from collections import deque

dist[X0][Y0] = 0
todo = deque([(X0, Y0)]) # 始点の設定

while todo:
    row, col = todo.popleft()
    for dy, dx in d:
        ni, nj = row + dy, col + dx
        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "W":
            if dist[ni][nj] != -1:
                continue
            dist[ni][nj] = dist[row][col] + 1
            todo.append((ni, nj))
            
    if dist[X1][Y1] != -1:
        print(dist[X1][Y1])
        exit()