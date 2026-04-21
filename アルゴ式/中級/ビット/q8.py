"""
フラグがどれか立っているか
(https://algo-method.com/tasks/1728pmHE)
"""

a,m = map(int, input().split())
print("Yes" if a & m else "No")