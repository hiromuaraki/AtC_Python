"""
ゲーム盤の回転
(https://algo-method.com/tasks/1257Tz4a)

回転前後どちらにおいてもコマが置かれているマスの個数
＝２つの共通しているマス
"""
H,W,N = map(int, input().split())

A,B = set(), set()

for _ in range(N):
    x,y = map(int, input().split())
    A.add((x, y))
    B.add((H - 1 - x, W - 1 - y))

print(len(A & B))