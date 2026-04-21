"""
フラグ状態を整数値にする (2)
(https://algo-method.com/tasks/1144ob2M)
"""

n = int(input())
F = list(map(int, input().split()))
print(sum(1 << f for f in F))
# ans = 0
# for f in F:
#   ans += 1 << f
# print(ans)