"""
B問題_Taro
"""

n,m = map(int, input().split())
child = [0] * n
for _ in range(m):
  a,b = input().split()
  a = int(a) - 1
  if b == "M" and child[a] == 0:
    child[a] += 1
    print("Yes")
  else:
    print("No")