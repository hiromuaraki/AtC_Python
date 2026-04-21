"""
フラグ状態の復元 (1)
(https://algo-method.com/tasks/1145k6W5)

and
"""

n,x = map(int, input().split())
print("Yes" if n & (1 << x) else "No")