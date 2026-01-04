n = int(input())
a = list(map(int ,input().split()))

max_len = 1
current = 1 # 現在の昇順区間の長さ
for i in range(n - 1):
  if a[i] <= a[i + 1]:
    current += 1
  else:
    current = 1
  max_len = max(max_len, current)
print(max_len)