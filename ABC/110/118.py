"""
B問題_Foods Loved by Everyone 
"""

n,m = map(int, input().split())
k = [0] * m
for _ in range(n):
  a = list(map(int, input().split()))
  for a_i in a[1:]:
    k[a_i - 1] += 1

print(k.count(n))




  