"""
【グラフ（無向グラフ）】

"""

N,M = map(int, input().split())
G = [[] * N for _ in range(N)]

for _ in range(M):
  a,b = map(int, input().split())
  a -= 1; b -= 1
  G[a].append(b)
  G[b].append(a)

ans = 0
for i in range(len(G)):
  count = 0
  for v in G[i]:
    if v < i + 1:
      count += 1
  if count == 1:
    ans += count

print(ans)