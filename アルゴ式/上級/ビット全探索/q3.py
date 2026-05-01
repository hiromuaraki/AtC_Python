"""
要素数
(https://algo-method.com/tasks/1137NCpt)
"""

n,x = map(int, input().split())
print(sum(1 for i in range(n) if x & (1 << i)))