"""
A問題_Growth Record
(https://atcoder.jp/contests/abc259/tasks/abc259_a)
難しい（区間問題）
"""

n,m,x,t,d = map(int, input().split())
if m >= x: print(t)
else : print(t - (x - m) * d)