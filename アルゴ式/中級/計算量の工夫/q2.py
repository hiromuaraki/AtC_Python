"""
1 個除外した総和の最大値
和を最大化する
"""
n = int(input())
a = sorted(map(int, input().split()), reverse=True)
print(sum(a[:len(a) - 1]))