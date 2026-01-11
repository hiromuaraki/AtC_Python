"""
B問題_Delimiter
"""
a = []
while True:
  n = int(input())
  a.append(n)
  if n == 0: break

print(*a[::-1], sep="\n")


