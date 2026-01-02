"""
B問題_SameName
"""


n = int(input())
names = set()
for _ in range(n):
  s, t = input().split()
  if (s, t) in names:
    print("Yes")
    exit()
  names.add((s, t))
print("No")