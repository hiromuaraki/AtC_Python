"""
グループ分け (1)
(https://algo-method.com/tasks/2f391c217964f112)

条件：グループに含まれる最小の整数を m としたとき、
グループに含まれる整数は 全て m の倍数である。

まだ使われていない最小の値から
その倍数を全部まとめて潰していく

選び方が局所最適かどうか
"""

n = int(input())
a = sorted(map(int, input().split()))
st = set()
count = 0
for i in range(n):
  if len(st) == n:
    break
  ok = False
  for j in range(n):
    if a[j] % a[i] == 0 and a[j] not in st:
      st.add(a[j])
      ok = True
  if ok:
    count += 1
print(count)


n = int(input())
a = set(map(int, input().split()))
ret = 0
# 別解
while len(a) > 0:
  ret += 1
  min_val = min(a)
  a = set(a_i for a_i in a if a_i % min_val != 0)
print(ret)



