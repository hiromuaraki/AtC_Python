"""
挿入、削除、検索 (1)
(https://algo-method.com/tasks/829)
"""

n = int(input())
a = list(map(int, input().split()))
  
q = int(input())
for _ in range(q):
  query = list(map(int, input().split()))
  k = query[1]
  if query[0] == 0:
    a.insert(k, query[2])
  elif query[0] == 1:
    a.pop(k)
  else:
    print(a.count(k))