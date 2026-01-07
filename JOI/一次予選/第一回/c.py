"""
共通要素 (Common Elements) 

集合（積集合）
集合a, b共通の要素を昇順で出力
"""

n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*sorted(a & b), sep="\n")