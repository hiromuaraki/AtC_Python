n = int(input())
d = list(map(int, input().split()))

for i in range(n - 1):
  dist = []
  for j in range(i + 1, n):
    dist.append(sum(d[i : j]))
  print(*dist)