"""
A問題_Adjacent Squares
(https://atcoder.jp/contests/abc250/tasks/abc250_a)

上下左右の4近傍の問題
"""

h,w = map(int, input().split())
r,c = map(int, input().split())
r -= 1; c -= 1

ans = 0
if r - 1 >= 0: ans += 1
if r + 1 < h: ans += 1
if c - 1 >= 0: ans += 1
if c + 1< w: ans += 1
print(ans)