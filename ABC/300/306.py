"""
B問題_Base 2

64ビット（64-bit）の符号なし整数（unsigned integer）を2進数表現から10進数へ変換する式
A0 * 2^0 + A1 * 2^1 + A2 * 2^2+ .... A63 * 2^63
"""

a = list(map(int, input().split()))
total = 0
for i in range(64):
  total += a[i] * 1 << i
print(total)
