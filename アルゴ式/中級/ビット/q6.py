"""
まとめてフラグを消す
(https://algo-method.com/tasks/17297Xhy)
~：not演算子
18 = 10010
11 = 01011 → 10100
"""

a,m = map(int, input().split())
print(a & ~m)