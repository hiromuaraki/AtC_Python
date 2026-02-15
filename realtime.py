n, k = map(int, input().split())
count = 0
for i in range(n):
  count += min(n, k // (i + 1))
print(count)