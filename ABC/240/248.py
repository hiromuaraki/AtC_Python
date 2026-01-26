"""
A問題_Lacked Number
"""

s = set(map(int, input()))
t = set(list(range(0, 10)))
print(*t - s)