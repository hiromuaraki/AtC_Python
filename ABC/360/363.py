"""
B問題_Japanese Cursed Doll
シミュレーション
"""

n,t,p = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
while True:
  count = 0
  for i in range(n):
    if l[i] >= t:
      count += 1
    l[i] += 1
  if count >= p:
    break
  ans += 1
  
print(ans)