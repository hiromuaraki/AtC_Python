"""
B問題_Not Found
"""

s = set(input())
t = set(chr(ord('a') + i) for i in range(26))
print(min(*t - s) if len(t - s) != 0 else "None")