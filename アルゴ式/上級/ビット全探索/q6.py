"""
差集合
(https://algo-method.com/tasks/1140jP10)
S - S∩T
"""

n,x,y = map(int, input().split())
print(x - (x & y))