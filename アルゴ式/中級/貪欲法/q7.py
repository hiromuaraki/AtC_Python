"""
部分列チェッカー
(http://algo-method.com/tasks/ec9cff3176b54b53)

順序は変えてはダメ
離れた文字をつなげてもOK
文字列は連続していなくてもいい
"""

n,m = map(int, input().split())
s = input()
t = input()

k = 0
for i in range(n):
  if k < m and s[i] == t[k]:
    k += 1
  if m == k:
    print("Yes")
    exit()
print("No")
