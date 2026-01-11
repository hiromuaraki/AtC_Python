"""
B問題_Coins
(https://atcoder.jp/contests/abc087/tasks/abc087_b)

変数を削る
a: 500
b: 100
c: 50

500a + 100b + 50c = x
50c = x - (500a + 100b)
a + b + c >= 0


"""


line = [int(input()) for _ in range(4)]
a,b,c,x = line
count = 0

# 0 <= x - (500a + 100b) <= 50cの（i, j）組を全探索
# O(N^2)
for i in range(a + 1):
  for j in range(b + 1):
    if 0 <= x - (500*i + 100*j) <= 50*c:
      count += 1

# 全探索
# for i in range(a + 1):
#   for j in range(b + 1):
#     for k in range(c + 1):
#       if 500*i + 100*j + 50*k == x:
#         count += 1
print(count)