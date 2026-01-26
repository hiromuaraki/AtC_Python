"""
A問題_Exponential Plant
(https://atcoder.jp/contests/abc354/tasks/abc354_a)
シミュレーション
"""

h = int(input())
c = 0
ans = 0
for i in range(h + 1):
  c += 2**i
  if c > h:
    ans = i + 1
    break
print(ans)


"""
B問題_AtCoder Janken 2
"""

n = int(input())
t = 0
lst = []
for _ in range(n):
  s,c = input().split()
  lst.append(s)
  t += int(c)

print(sorted(lst)[t % n])