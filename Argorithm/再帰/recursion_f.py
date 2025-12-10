"""
sum_of_digits
1桁ずつ分解し1桁になるまで足すことを繰り返す

文字列で入力を受け取る＝リスト型に変換する為
整数型のリストに変換し合計を求める
合計した結果が10桁以上＝2桁以上のため、1桁になるまで上記処理を繰り返す

"""

N = input()

def sum_of_digits(num):
  num = sum(list(map(int, num)))
  if num >= 10:
    return sum_of_digits(str(num))
  return num

print(sum_of_digits(N))


"""
最大公約数を求める
ユークリッドの互除法
"""

def gcd(x, y):
  if y == 0:
    return y
  return gcd(y, x%y)


"""
N!
n * (n-1)*(n-2)*(n-3)..2*1
N=5の場合：
1*2*3*4*5=120
"""

def func(n):
  if n == 1:
    return 1
  return n * func(n - 1)


"""
総和
"""

def sum_func(n):
  if n == 0:
    return 0
  return n + sum_func(n - 1)


"""
フィボナッチ数列
f(n) = f(n-1) + f(n-2)
前の2つの項の和の数列
"""

def fib(n):
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2) # 同じ計算を何度もしてしまう