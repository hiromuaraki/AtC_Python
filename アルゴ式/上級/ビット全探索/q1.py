"""
集合を表す整数値 (2)
(https://algo-method.com/tasks/1126pQ7q)
"""

n,k = map(int, input().split())
s = set(map(int, input().split()))
print(sum(1 << s_i for s_i in s ))
    