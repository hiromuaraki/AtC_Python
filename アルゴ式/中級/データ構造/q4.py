"""
積ん読
(https://algo-method.com/tasks/b0d53a6d2ea991ed)

スタック（stack）
"""
q = int(input())
stack = []
for _ in range(q):
  query = list(input().split())
  if int(query[0]) == 1:
    stack.append(query[1])
  else:
    print(stack.pop())

