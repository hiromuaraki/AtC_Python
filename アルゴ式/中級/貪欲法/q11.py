"""
荷物と箱
(https://algo-method.com/tasks/361)

荷物を順番に見る
その荷物を詰められるいちばん 先に空いている箱 に入れる
箱を埋めたらもう使わない
"""

from collections import deque

n,m = map(int, input().split())
a = list(map(int, input().split())) # 荷物の重さ
b = list(map(int, input().split())) # 箱の制限容量
box = [False] * m 
deq = deque(a)
while deq:
  val = deq.popleft()
  for i in range(m):
    if val <= b[i] and not box[i]:
      box[i] = True
      break
print(sum(box))
