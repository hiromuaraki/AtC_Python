"""
Linux の権限
(https://algo-method.com/tasks/1699e2Ts)
"""

x = input()
P,Q = input().split()
user = {"o": 0, "g": 1, "u": 2}[P]
ans = {"r": 0, "w": 1, "x": 2}[Q]
s = ""
n = int(user)
for _ in range(3):
  s = str(n % 2) + s
  n //= 2
print("Yes" if s[ans] == "1" else "No")


# 別解
x = input()
P,Q = input().split()
user = {"o": 0, "g": 1, "u": 2}[P]
ans = {"r": 2, "w": 1, "x": 0}[Q]

n = int(x[user])
print("Yes" if (n >> ans) & 1 else "No")