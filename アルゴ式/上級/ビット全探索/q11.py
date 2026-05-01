"""
Ex. ライツアウト
(https://algo-method.com/tasks/10888fQi)
O(2^HW)

保留
"""
h,w = map(int, input().split())
s = [input() for _ in range(h)]
grid = [[0] * w for _ in range(h)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            grid[i][j] = 1

for S in range(2 ** (h*w)):
    for x in range(h):
        for y in range(w):
            id = x * w + y

            if S & (1 << id):
                for dx, dy in d:
                    ni, nj = x + dx, y + dy
                    if 0 <= ni < h and 0 <= nj < w:
                        grid[ni][nj] ^= 1
