"""
塊の個数
(https://algo-method.com/tasks/1381Q36X)

座標(i, j)をそのまま頂点として扱う
"""

H,W = map(int, input().split())
S = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y: int, x: int):
    visited[y][x] = True
    
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < H and 0 <= nx < W):
            continue
        if S[ny][nx] == "#" and not visited[ny][nx]:
            dfs(ny, nx)

count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#" and not visited[i][j]:
            dfs(i, j)
            count += 1
print(count)

