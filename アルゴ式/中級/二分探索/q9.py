"""
ひもを切る
(https://algo-method.com/tasks/369)
"""
n, k = map(int, input().split())
l = list(map(float, input().split()))

def f(x, L):
  total = 0
  for l_i in L:
    total += int(l_i / x)
  return total

left = 0
right = 10**5
while right - left > 1e-8: 
  mid = (left + right) / 2
  if f(mid,l) >= k:
    left = mid
  else:
    right = mid
print(left)