"""
B問題_Qualification Contest
(https://atcoder.jp/contests/abc288/tasks/abc288_b)

辞書順
"""

n,k = map(int, input().split())
s = [input() for _ in range(n)]
print(*sorted(s[:k]), sep="\n")