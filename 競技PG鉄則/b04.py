"""
Binary Representation 2
"""

n = input()
ans = 0
L = len(n)
for i in range(L):
  ans += int(n[L - 1 - i]) * (1 << i)
print(ans)