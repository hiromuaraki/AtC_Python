"""
B問題_Trimmed Mean

ソート＋スライス

集合A：n...|x|-1
集合B：0...|集合A|-n
"""

n = int(input())
x = sorted(map(int, input().split()))
a = x[n:]
b = a[:-n]
print(sum(b) / (len(x) - 2*n))
