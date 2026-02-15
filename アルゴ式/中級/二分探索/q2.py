"""
貯金 (1)
(https://algo-method.com/tasks/367)

十分な制度になるまで
"""

n,m = map(float, input().split())
 
def f(N: float, x: float):
  """0(今年）〜 5年後までの預金額をシミュレーションする関数"""
  result = N + 1
  for _ in range(5):
    result = result * x + 1
  return result

ok = 0
ng = 100
# 半回区間[ok, ng)
while (ng - ok > 1e-4):
  mid = (ok + ng) / 2 # 精度を十分にするまで浮動小数点で対応
  if f(n, mid) < m:
    ok = mid
  else:
    ng = mid
print(ok)
    