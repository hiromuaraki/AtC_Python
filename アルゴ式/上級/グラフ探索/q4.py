"""
デッドロック
(https://algo-method.com/tasks/536)
課題を終えているか管理する方法＝キュー

sum(depend) = 残り依存総数
done = 課題完了数
"""

from collections import deque
N,M = map(int, input().split())
G = [[] for _ in range(N)]
depend = [0] * N # 残り必要条件の数 -> 0になった瞬間に着手可能

for _ in range(M):
    F,S = map(int, input().split())
    G[F].append(S)
    depend[S] += 1

todo = deque(i for i in range(N) if depend[i] == 0)
done = 0 # 完了済み課題数を記録

while todo:
    t = todo.popleft()
    done += 1
    for i in G[t]:
        depend[i] -= 1
        if depend[i] == 0:
            todo.append(i)
print("Yes" if done == N else "No")