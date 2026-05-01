"""
反転
(https://algo-method.com/tasks/831)

・数列を左右反転
・末尾追加
・末尾削除
"""

n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
  query_type = list(map(int, input().split()))
  if query_type[0] == 0:
    a = a[::-1]
  elif query_type[0] == 1:
    a.append(query_type[1])
  else:
    print(a.pop() if a else "Error")