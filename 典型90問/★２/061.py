"""
【deque（高速なデータ構造の処理）】

deque・・・先頭と末尾の要素を高速に追加、削除を行うデータ構造
キューの一種
"""

from collections import deque

Q = int(input())
deq = deque()
for _ in range(Q):
  t,x = map(int, input().split())
  
  if t == 1:
    deq.appendleft(x)
  elif t == 2:
    deq.append(x)
  else:
    print(deq[x - 1])
