"""
フラグがすべて立っているか
(https://algo-method.com/tasks/1731mYh4)

「M ⊆ A か？」
M ⊆ A ? 包含判定 → new✨
"""

a,m = map(int, input().split())
print("Yes" if a & m == m else "No")