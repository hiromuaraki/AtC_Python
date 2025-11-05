"""
【N進法展開】
8新数→9進数へ変換
N=0のケースは０を出力
"""

N,K = input().split()
print(int(N, 8))
K = int(K)

for _ in range(K):
  n = int(N, 8)
  res = ""
  if n == 0:
    res = "0"
  
  while n > 0:
    # ８進数→9進数へ変換
    res = str(n % 9) + res
    n //= 9
  res = res.replace("8", "5")
  N = res
print(N)