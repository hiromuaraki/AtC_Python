"""
A問題_ABC400 Party
"""

N = int(input())
print(400//N if 400 % N == 0 else -1)


"""
B問題_Sum of Geometric Series・・・・解けた
難易度33
問題文をちゃんと読む
"""

N,M = map(int, input().split())
INF = 10**9
x = 0
for i in range(M + 1):
  x += N**i
print(x if x <= INF else "inf")