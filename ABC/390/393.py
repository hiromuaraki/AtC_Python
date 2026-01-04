"""
B問題_A..B..C

全探索
O(N^3)

等間隔に並んでいるA,B,Cの組み(i, j, k)の数え上げ
例）n = 5

i - j = k - jは(i, j, k)が等間隔かを見ている
k = 2j - iに式変形できる
"""

s = input()
n = len(s)
count = 0
# O(N^3)
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      if j - i != k - j: continue
      if s[i] + s[j] + s[k] == "ABC":
        count += 1

# O(N^2)
for i in range(n):
  for j in range(i + 1, n):
    k = 2*j - i
    if k >= n: continue
    if s[i] + s[j] + s[k] == "ABC":
      print(i + 1, j + 1, k + 1)
      count += 1
print(count)