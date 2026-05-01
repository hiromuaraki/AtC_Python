"""
ナップサック問題
(https://algo-method.com/tasks/11333SSl)

ビット全探索
"""

n,m = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

ans = 0
# 部分集合を列挙
for S in range(1 << n): # 2^N通り試す（選ぶ／選ばない）
    total = 0
    cost = 0
    for i in range(n):
        if S & (1 << i):
            total += w[i]
            cost += v[i]
    if total <= m:
        ans = max(ans, cost)
print(ans)
        
