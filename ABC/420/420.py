"""
A問題_What month is it?・・・解けた
難易度10
"""

X,Y = map(int, input().split())
ans = (X + Y)%12
print(ans if ans != 0 else 12)


"""
B問題_Most Minority・・・解けた
難易度74
"""

N,M = map(int, input().split())
S = [input() for _ in range(N)]
cnt = [0] * N
ns = []
for j in range(M):
  t = ""
  for i in range(N):
    t += S[i][j]
  ns.append(t)

for i in range(M):
  str_n = list(ns[i])
  zero = str_n.count("0")
  for j in range(N):
    if zero == M or zero == 0:
      cnt[j] += 1
    else:
      one = N - zero
      hum = ("0" if zero < one else "1")
      if str_n[j] == hum:
        cnt[j] += 1

mx = max(cnt)
for i in range(N):
  if mx == cnt[i]:
    print(i + 1, end=" ")