"""
D問題_284_Happy New Year 2023・・・解けない
難易度658

素因数分解
"""

T = int(input())
for i in range(T):
  N = int(input())
  p = 2
  while p * p <= N:
    if N % p == 0:
      N //= p
      break
    p += 1
  if N % p == 0:
    print(p, N // p)
  else:
    print(int(N**0.5), p) 


"""
問題011_PrintPrimeNumbers・・・解けた
難易度6Q
アルゴリズム×数学

N以下の素数を列挙

素数とは
・1と自分自身の数でしか割れない数＝約数が２個
"""

N = int(input())

def is_prime(n):
  """素数を判定"""
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in range(2, N + 1):
  if is_prime(i):
    print(i)

"""
問題_012_Primality Test・・・解けた
難易度５Q

素数判定
Nが素数であるかどうかを判定

2..√N回の範囲を回す(自分自身を含めない)
"""

N = int(input())
for i in range(2, int(N**0.5)):
  if N % i == 0:
    print("No")
    exit()
print("Yes")


"""
問題014_Factorization・・・ギリ解けた
難易度5Q

計算量：O(√N）
素因数分解

素数で割れるまで繰り返す＝素因数分解
Nが1で終わらないケースは、素数で割れるため、
末尾にNを追加することで素因数分解できる

例）N=10
2 * 5 = 10としたい
10 % 2 = 0
5 % 2 割れない
5 % 3 割れない

この時点でのN=5は2以上だから
Nを追加
"""

N = int(input())

ans = []
for i in range(2, int(N**0.5) + 1):
  while N % i == 0:
    ans.append(i)
    N //= i
# 最後の数を追加
if N >= 2:
  ans.append(N)
print(*ans)