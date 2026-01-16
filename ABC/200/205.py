"""
B問題_Permutation Check
"""

n = int(input())
a = sorted(map(int, input().split()))
b = list(range(1, n + 1))
print("Yes" if a == b else "No")