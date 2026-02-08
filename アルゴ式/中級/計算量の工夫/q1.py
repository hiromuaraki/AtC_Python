"""
差の最大値

差を最大化する
最大値−最小値
"""

n = int(input())
a = sorted(map(int, input().split()))
print(a[-1] - a[0])
