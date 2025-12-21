"""
等比数列・・・解けた
初項 * 公比 ** (N-1)

R==1の場合は等比が1の為10^9回る
R==1の場合は等比1なのでAを出力
"""

A,R,N=map(int, input().split())

def geometric(a, r, n):
  func = a
  for _ in range(n):
    if r == 1: return A
    
    func *= r
    if func > 10**9: return "large"
  
  return func

print(geometric(A,R,N-1))