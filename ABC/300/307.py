"""
B問題_racecar
全探索

(https://atcoder.jp/contests/abc307/tasks/abc307_b)
"""

n = int(input())
s = [input() for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j: continue
    t = s[i] + s[j]
    if t == t[::-1]:
      print("Yes")
      exit()
print("No")
